"""
Test Harness — Modal Lattice Operator
Structural, non-interpretive.

Ensures:
- judicial vs administrative classification runs
- output structure is stable
"""

import json
from operators.modal_lattice import ModalLatticeOperator

def test_modal_lattice_basic():
    with open("visual-grammar.json") as f:
        grammar = json.load(f)

    op = ModalLatticeOperator(grammar)
    result = op.classify_constraints()

    assert "judicial" in result
    assert "administrative" in result
    assert isinstance(result["judicial"], list)
    assert isinstance(result["administrative"], list)
