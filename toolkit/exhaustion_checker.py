"""
Exhaustion Checker
------------------
Checks structural completeness for Stage-1.
Structural, non-interpretive.
"""

class ExhaustionChecker:
    def __init__(self, grammar, operator_results):
        self.grammar = grammar
        self.results = operator_results

    def check(self):
        return {
            "nodes_present": len(self.grammar["nodes"]) > 0,
            "edges_present": len(self.grammar["edges"]) > 0,
            "surfaces_present": len(self.grammar["surfaces"]) > 0,
            "operators_ran": all(k in self.results for k in [
                "holonomy", "modal_lattice", "collapse_surface", "spectral_bundle"
            ])
        }
