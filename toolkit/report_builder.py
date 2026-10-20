"""
Report Builder
--------------
Assembles operator outputs into a unified structural report.
Structural, non-interpretive.
"""

class ReportBuilder:
    def __init__(self, operator_results):
        self.results = operator_results

    def build(self):
        return {
            "holonomy_loops": self.results["holonomy"],
            "modal_lattice_map": self.results["modal_lattice"],
            "collapse_surface_report": self.results["collapse_surface"],
            "spectral_bundle_map": self.results["spectral_bundle"]
        }
