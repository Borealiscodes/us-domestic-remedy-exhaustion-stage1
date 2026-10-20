"""
Grammar Loader
--------------
Loads and validates the visual grammar JSON file.
Structural, non-interpretive.
"""

import json

class GrammarLoader:
    def __init__(self, path="visual-grammar.json"):
        self.path = path
        self.grammar = None

    def load(self):
        with open(self.path) as f:
            self.grammar = json.load(f)
        return self.grammar

    def get(self):
        if self.grammar is None:
            return self.load()
        return self.grammar
