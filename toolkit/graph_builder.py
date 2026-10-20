"""
Graph Builder
-------------
Constructs a simple adjacency representation of the grammar.
Structural, non-interpretive.
"""

class GraphBuilder:
    def __init__(self, grammar):
        self.grammar = grammar

    def build(self):
        graph = {}
        for node in self.grammar["nodes"]:
            graph[node["id"]] = []

        for edge in self.grammar["edges"]:
            graph[edge["from"]].append(edge["to"])

        return graph
