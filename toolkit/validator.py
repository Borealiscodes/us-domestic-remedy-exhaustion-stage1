"""
Grammar Validator
-----------------
Ensures nodes, edges, and surfaces follow structural rules.
Structural, non-interpretive.
"""

class GrammarValidator:
    def __init__(self, grammar):
        self.grammar = grammar

    def validate_nodes(self):
        assert isinstance(self.grammar["nodes"], list)
        for n in self.grammar["nodes"]:
            assert "id" in n
            assert "layer" in n

    def validate_edges(self):
        assert isinstance(self.grammar["edges"], list)
        for e in self.grammar["edges"]:
            assert "from" in e
            assert "to" in e
            assert "type" in e

    def validate_surfaces(self):
        assert isinstance(self.grammar["surfaces"], list)
        for s in self.grammar["surfaces"]:
            assert "id" in s
            assert "nodes" in s

    def run_all(self):
        self.validate_nodes()
        self.validate_edges()
        self.validate_surfaces()
        return True
