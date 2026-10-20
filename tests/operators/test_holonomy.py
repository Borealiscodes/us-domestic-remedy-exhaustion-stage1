"""
Test Harness — Holonomy Operator
Structural, non-interpretive.

Ensures:
- grammar loads
- operator initializes
- loops are detected without error
"""

import json
from operators.holonomy import HolonomyOperator

def test_holonomy_basic():
    with open("visual-grammar.json") as f:
        grammar = json.load(f)

    op = HolonomyOperator(grammar)
    loops = op.find_loops()

    assert isinstance(loops, list)
    for loop in loops:
        assert isinstance(loop, list)
        assert len(loop) >= 2
