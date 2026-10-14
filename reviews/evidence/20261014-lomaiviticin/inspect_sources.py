import csv
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml
from rdkit import Chem, rdBase
from rdkit.Chem import Descriptors, Draw, rdMolDescriptors

W = Path(__file__).parent


def sha(value):
    return hashlib.sha256(value).hexdigest()


def qualifiers(feature):
    return {q.findtext('GBQualifier_name'): q.findtext('GBQualifier_value')
            for q in feature.findall('GBFeature_quals/GBQualifier')}


capture = json.loads((W / 'capture.json').read_text())
prior = json.loads(Path(capture['prior_checkpoint']).read_text())
for row in prior['records']:
    assert sha(Path(row['path']).read_bytes()) == row['sha256']
    for component in row['graph_components']:
        assert sha(Path(component['path']).read_bytes()) == component['sha256']
for row in prior['all_review_observations']:
    for key in ('yaml', 'markdown'):
        assert sha(Path(row[key]).read_bytes()) == row[key + '_sha256']
assert rdBase.rdkitVersion == '2026.03.5'
out = {'rdkit_version': rdBase.rdkitVersion, 'verified_owners': 3115,
       'verified_components': 243, 'verified_prior_bundles': 79, 'records': []}
with Path('data/raw/mibig_compounds.tsv').open() as handle:
    mibig = list(csv.DictReader(handle, delimiter='\t'))
with Path('data/raw/npclassifier.tsv').open() as handle:
    classes = list(csv.DictReader(handle, delimiter='\t'))
for target in capture['targets']:
    path = Path(target['path'])
    doc = yaml.safe_load(path.read_text())
    structure = doc['chemical_structure']
    mol = Chem.MolFromSmiles(structure['smiles'])
    assert mol is not None
    key = Chem.MolToInchiKey(mol)
    assert key == structure['standard_inchi_key']
    assert Chem.MolToInchi(mol) == structure['standard_inchi']
    centers = Chem.FindMolChiralCenters(mol, includeUnassigned=True, useLegacyImplementation=False)
    raw_rows = [r for r in mibig if r['standard_inchi_key'] == key]
    assert len(raw_rows) == 1
    raw = raw_rows[0]
    live = json.loads((W / (raw['mibig_accession'] + '.5.json')).read_text())
    compound = live['compounds'][int(raw['compound_index']) - 1]
    assert compound['name'] == doc['label']
    live_mol = Chem.MolFromSmiles(compound['structure'])
    assert Chem.MolToInchiKey(live_mol) == key
    classified = [r for r in classes if r['standard_inchi_key'] == key]
    assert len(classified) == 1
    rings = mol.GetRingInfo().AtomRings()
    core_rings = []
    for ring in rings:
        if len(ring) != 6 or any(mol.GetAtomWithIdx(i).GetAtomicNum() != 6 for i in ring):
            continue
        descriptions = []
        has_oxo = has_quaternary_ether = False
        for idx in ring:
            atom = mol.GetAtomWithIdx(idx)
            extras = [n for n in atom.GetNeighbors() if n.GetIdx() not in ring]
            labels = []
            for neighbor in extras:
                bond = mol.GetBondBetweenAtoms(idx, neighbor.GetIdx())
                if neighbor.GetAtomicNum() == 8 and bond.GetBondTypeAsDouble() == 2:
                    labels.append('carbonyl')
                    has_oxo = True
                elif neighbor.GetAtomicNum() == 8 and neighbor.GetDegree() == 2:
                    label = 'quaternary_ether' if atom.GetTotalNumHs() == 0 else 'secondary_ether'
                    labels.append(label)
                    has_quaternary_ether |= label == 'quaternary_ether'
                elif neighbor.GetAtomicNum() == 6 and atom.GetHybridization() == Chem.HybridizationType.SP3:
                    if any(neighbor.GetIdx() in r and len(r) == 6 and r != ring for r in rings):
                        labels.append('intercore_bridge')
            descriptions.append({'atom_index': idx, 'H': atom.GetTotalNumHs(),
                                 'attachments': labels})
        if has_oxo and has_quaternary_ether:
            core_rings.append(descriptions)
    image = W / (path.stem + '-structure.png')
    Draw.MolToFile(mol, str(image), size=(1400, 1000), legend=path.stem + ' | ' + key)
    out['records'].append({
        'path': str(path), 'identifier': doc['identifier'], 'key': key,
        'formula': rdMolDescriptors.CalcMolFormula(mol),
        'exact_mass': Descriptors.ExactMolWt(mol),
        'formal_charge': Chem.GetFormalCharge(mol),
        'unassigned_centers': [idx for idx, stereo in centers if stereo == '?'],
        'stereo_complete_flag': structure['stereo_complete'],
        'raw_row': raw,
        'raw_row_sha256': sha(json.dumps(raw, sort_keys=True, separators=(',', ':')).encode()),
        'classification_row': classified[0],
        'live_mibig_status': live['status'], 'live_structure_matches': True,
        'core_ring_paths': core_rings, 'depiction': str(image),
        'depiction_sha256': sha(image.read_bytes()),
    })
out['taxonomy'] = []
for taxon in ET.parse(W / 'taxonomy.xml').findall('Taxon'):
    out['taxonomy'].append({k: taxon.findtext(k) for k in
                            ['TaxId', 'ScientificName', 'Rank', 'ParentTaxId', 'Lineage']})
out['loci'] = []
locus_sequences = {}
for filename in ['pacifica-loci.xml', 'tropica-locus.xml']:
    for locus in ET.parse(W / filename).findall('GBSeq'):
        row = {k: locus.findtext('GBSeq_' + k) for k in
               ['accession-version', 'definition', 'length']}
        row['source'] = qualifiers(locus.find('.//GBFeature[GBFeature_key="source"]'))
        row['proteins'] = []
        for feature in locus.findall('.//GBFeature[GBFeature_key="CDS"]'):
            q = qualifiers(feature)
            if (q.get('gene') in ('lom62', 'lom63')
                    or q.get('locus_tag') in ('Strop_2223', 'lom62', 'lom63')):
                row['proteins'].append({'location': feature.findtext('GBFeature_location'), **q})
                locus_sequences[q['protein_id']] = q['translation'].upper()
        out['loci'].append(row)
out['proteins'] = []
for protein in ET.parse(W / 'proteins.xml').findall('GBSeq'):
    accession = protein.findtext('GBSeq_accession-version')
    sequence = protein.findtext('GBSeq_sequence').upper()
    source = qualifiers(protein.find('.//GBFeature[GBFeature_key="source"]'))
    cds = qualifiers(protein.find('.//GBFeature[GBFeature_key="CDS"]'))
    assert sequence == locus_sequences[accession]
    out['proteins'].append({'accession': accession, 'source': source,
                            'cds': cds, 'length': len(sequence),
                            'sequence_sha256': sha(sequence.encode()),
                            'matches_deposited_translation': True})
uniprot = json.loads((W / 'A4X724.json').read_text())
assert uniprot['sequence']['value'] == locus_sequences['ABP54674.1']
out['A4X724_sequence_matches_ABP54674_1'] = True
out['uniprot_exact_search_results'] = len(json.loads((W / 'uniprot-lom-exact.json').read_text())['results'])
out['pair_sequence_identity'] = {
    'Lom62_DPJ0016_vs_DPJ0019': locus_sequences['AHZ61896.1'] == locus_sequences['AHF72798.1'],
    'Lom63_DPJ0016_vs_DPJ0019': locus_sequences['AHZ61897.1'] == locus_sequences['AHF72799.1'],
}
out['inventory_matches'] = {}
keys = {row['key'] for row in out['records']}
for name in ['chebi_structures', 'chebi_origins', 'lotus_occurrences',
             'pubchem_bioassay', 'bindingdb_targets', 'antibioticmech_inchikeys']:
    matches = []
    with Path('data/raw/' + name + '.tsv').open() as handle:
        for number, row in enumerate(csv.DictReader(handle, delimiter='\t'), 2):
            if keys.intersection(row.values()):
                matches.append({'line': number, 'row': row,
                                'sha256': sha(json.dumps(
                                    row, sort_keys=True, separators=(',', ':')).encode())})
    out['inventory_matches'][name] = matches
(W / 'source-analysis.json').write_text(json.dumps(out, indent=2))
print(json.dumps(out, indent=2))
