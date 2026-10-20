"""
Surface Mapper
--------------
Maps nodes to surfaces for structural analysis.
Structural, non-interpretive.
"""

class SurfaceMapper:
    def __init__(self, grammar):
        self.grammar = grammar

    def map(self):
        mapping = {}
        for surface in self.grammar["surfaces"]:
            for node in surface["nodes"]:
                mapping.setdefault(node, []).append(surface["id"])
        return mapping
