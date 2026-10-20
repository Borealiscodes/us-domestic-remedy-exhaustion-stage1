"""
Test Harness — Collapse Surface Detector
Structural, non-interpretive.

Ensures:
- surfaces load correctly
- detector returns stable structural output
"""

import json
from operators.collapse_surface import CollapseSurfaceDetector

def test_collapse_surface_basic():
    with open("visual-grammar.json") as f:
        grammar = json.load(f)

    op = CollapseSurfaceDetector(grammar)
    surfaces = op.detect()

    assert isinstance(surfaces, list)
    for s in surfaces:
        assert "surface_id" in s
        assert "nodes" in s
        assert "description" in s
