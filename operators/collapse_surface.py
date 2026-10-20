"""
Collapse Surface Detector (Structural)
--------------------------------------
Identifies structural contradictions across surfaces:
- unmet nondiscretionary duties
- procedural barriers
- enforcement conflicts

This operator is procedural, not interpretive.
"""

class CollapseSurfaceDetector:
    def __init__(self, grammar):
        self.grammar = grammar

    def detect(self):
        """
        Returns a list of surfaces where contradictions may occur.
        """
        surfaces = []

        for surface in self.grammar["surfaces"]:
            surfaces.append({
                "surface_id": surface["id"],
                "nodes": surface["nodes"],
                "description": surface["description"]
            })

        return surfaces
