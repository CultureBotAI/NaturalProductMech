"""Report taxon overlap without assuming independent publication support."""

import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "np_report", Path(__file__).resolve().parents[1] / "scripts/np_report.py")
report = importlib.util.module_from_spec(spec)
spec.loader.exec_module(report)


def test_overlap_metric_is_not_independent_corroboration():
    records = [{
        "producer_organisms": [{"taxon_id": "NCBITaxon:666"}],
        "occurrences": [{"taxon_id": "NCBITaxon:666"}],
    }, {
        "producer_organisms": [{"taxon_id": "NCBITaxon:666"}],
        "occurrences": [{"taxon_id": "NCBITaxon:562"}],
    }]
    summary = report.summarize(records)
    assert summary["producers_corroborated_by_an_occurrence"] == 1
    text = report.render(summary)
    assert "independently corroborated" not in text
    assert "publication independence not assessed): 1" in text
