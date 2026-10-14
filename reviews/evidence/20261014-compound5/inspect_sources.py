import csv
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

from rdkit import Chem, rdBase
from rdkit.Chem import rdMolDescriptors

W = Path(__file__).parent
out = {'rdkit': rdBase.rdkitVersion, 'chemistry': {}, 'inventories': {}}
docs = {s: json.loads((W / (s + '-resolved.json')).read_text()) for s in ('compound-5', 'compound-5-2')}
keys = {d['chemical_structure']['standard_inchi_key'] for d in docs.values()}
for slug, doc in docs.items():
    structure = doc['chemical_structure']
    mol = Chem.MolFromSmiles(structure['smiles'])
    assert mol is not None
    data = dict(formula=rdMolDescriptors.CalcMolFormula(mol), charge=Chem.GetFormalCharge(mol),
                inchi=Chem.MolToInchi(mol), key=Chem.MolToInchiKey(mol),
                centers=Chem.FindMolChiralCenters(mol, includeUnassigned=True),
                double_bond_stereo=[str(b.GetStereo()) for b in mol.GetBonds() if b.GetBondType() == Chem.BondType.DOUBLE])
    assert data['inchi'] == structure['standard_inchi']
    assert data['key'] == structure['standard_inchi_key']
    assert structure['stereo_complete'] == all(c[1] != '?' for c in data['centers'])
    bgc = structure['structure_source_id'].split(':')[1]
    source = json.loads((W / (bgc + '.3.json')).read_text())
    matches = [(i + 1, c) for i, c in enumerate(source['compounds']) if c['structure'] == structure['smiles']]
    assert len(matches) == 1
    data['mibig_compound_index'] = matches[0][0]
    out['chemistry'][slug] = data
for name in ('mibig_compounds', 'lotus_occurrences', 'chebi_structures', 'chebi_origins', 'npclassifier', 'antibioticmech_inchikeys', 'pubchem_bioassay'):
    with open('data/raw/' + name + '.tsv') as handle:
        rows = list(csv.DictReader(handle, delimiter='\t'))
    out['inventories'][name] = dict(rows_scanned=len(rows), matches=[dict(row_number=i + 2, row=r) for i, r in enumerate(rows) if r.get('standard_inchi_key') in keys])
out['taxonomy'] = [dict(taxon_id=t.findtext('TaxId'), name=t.findtext('ScientificName'), rank=t.findtext('Rank'), lineage=t.findtext('Lineage'), other_names=[(n.tag, n.text) for n in t.findall('OtherNames/*') if n.text and n.text.strip()]) for t in ET.parse(W / 'taxonomy.xml').findall('Taxon')]
out['sequences'] = {}
for filename in ('CH445335.1-region.xml', 'DS027698.1-region.xml'):
    records = []
    for seq in ET.parse(W / filename).findall('GBSeq'):
        features = []
        for f in seq.findall('GBSeq_feature-table/GBFeature'):
            if f.findtext('GBFeature_key') not in ('source', 'CDS'):
                continue
            qualifiers = [(q.findtext('GBQualifier_name'), q.findtext('GBQualifier_value')) for q in f.findall('GBFeature_quals/GBQualifier') if q.findtext('GBQualifier_name') != 'translation']
            features.append(dict(key=f.findtext('GBFeature_key'), location=f.findtext('GBFeature_location'), qualifiers=qualifiers))
        records.append(dict(accession=seq.findtext('GBSeq_accession-version'), definition=seq.findtext('GBSeq_definition'), length=seq.findtext('GBSeq_length'), features=features))
    out['sequences'][filename] = records
(W / 'source-inspection.json').write_text(json.dumps(out, indent=2))
print(json.dumps(out['chemistry'], indent=2))
print('Inventory counts:', {n: (v['rows_scanned'], len(v['matches'])) for n,v in out['inventories'].items()})
print(json.dumps(out['taxonomy'], indent=2))
print(json.dumps(out['sequences'], indent=2))
