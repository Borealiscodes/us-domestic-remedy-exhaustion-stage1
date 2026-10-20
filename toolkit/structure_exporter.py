"""
structure_exporter.py — Structural Export Module
Exports nodes, flows, surfaces, and operator outputs into unified maps.
"""

class StructureExporter:
    def export(self, loader, operators):
        """Return a combined structural map."""
        return {
            "nodes": loader.nodes,
            "flows": loader.flows,
            "surfaces": loader.surfaces,
            "operators": list(operators.keys())
        }
