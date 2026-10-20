"""
Spectral Bundle Operator (Structural)
-------------------------------------
Maps interactions between:
- federal statutes
- municipal duties
- extraterritorial constraints

This operator is procedural, not interpretive.
"""

class SpectralBundleOperator:
    def __init__(self, grammar):
        self.grammar = grammar

    def map_interactions(self):
        """
        Returns a list of cross-layer interactions based on edges.
        """
        interactions = []

        for edge in self.grammar["edges"]:
            interactions.append({
                "from": edge["from"],
                "to": edge["to"],
                "type": edge["type"],
                "description": edge["description"]
            })

        return interactions
