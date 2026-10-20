"""
operator_registry.py — Operator Registration Module
Provides a unified interface for loading and managing Stage-1 operators.
"""

class OperatorRegistry:
    def __init__(self):
        self.registry = {}

    def register(self, name, operator):
        self.registry[name] = operator

    def get_all(self):
        return self.registry
