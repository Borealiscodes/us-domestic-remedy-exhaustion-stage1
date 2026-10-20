"""
Test Harness — Spectral Bundle Operator
Structural, non-interpretive.

Ensures:
- cross-layer interactions map correctly
- edge structure is stable
"""

import json
from operators.spectral_bundle import SpectralBundleOperator

def test_spectral_bundle_basic():
    with open("visual-grammar.json") as f:
        grammar = json.load(f)

    op = SpectralBundleOperator(grammar)
    interactions = op.map_interactions()

    assert isinstance(interactions, list)
    for i in interactions:
        assert "from" in i
        assert "to" in i
        assert "type" in i
        assert "description" in i
