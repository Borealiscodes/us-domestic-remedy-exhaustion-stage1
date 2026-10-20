"""
Modal Lattice Operator (Structural)
-----------------------------------
Separates judicial vs administrative acts.
Used to clarify mandamus prerequisites.

This operator is procedural, not interpretive.
"""

class ModalLatticeOperator:
    def __init__(self, grammar):
        self.grammar = grammar

    def classify_constraints(self):
        """
        Returns a dictionary separating judicial vs administrative constraints.
        """
        judicial = []
        administrative = []

        for node in self.grammar["nodes"]:
            if node["id"] == "N02":  # Judicial Branch Constraints
                judicial.append(node)
            # Future administrative nodes can be added here.

        return {
            "judicial": judicial,
            "administrative": administrative
        }
