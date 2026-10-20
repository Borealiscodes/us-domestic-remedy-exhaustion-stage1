"""
runtime.py — Stage-1 Runtime Orchestrator
Coordinates operator execution, loader initialization, and structural output routing.
"""

class Stage1Runtime:
    def __init__(self, loader, operators, reporter):
        self.loader = loader
        self.operators = operators
        self.reporter = reporter

    def run_all(self):
        """Execute all Stage-1 operators and route outputs."""
        results = {}
        for name, operator in self.operators.items():
            results[name] = operator.run(self.loader)
        self.reporter.write(results)
        return results
