"""
Operator Runner
---------------
Executes structural operators in a stable order.
Structural, non-interpretive.
"""

from operators.holonomy import HolonomyOperator
from operators.modal_lattice import ModalLatticeOperator
from operators.collapse_surface import CollapseSurfaceDetector
from operators.spectral_bundle import SpectralBundleOperator

class OperatorRunner:
    def __init__(self, grammar):
        self.grammar = grammar

    def run(self):
        results = {}

        results["holonomy"] = HolonomyOperator(self.grammar).find_loops()
        results["modal_lattice"] = ModalLatticeOperator(self.grammar).classify_constraints()
        results["collapse_surface"] = CollapseSurfaceDetector(self.grammar).detect()
        results["spectral_bundle"] = SpectralBundleOperator(self.grammar).map_interactions()

        return results
