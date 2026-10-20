"""
Holonomy Operator (Structural)
------------------------------
Detects jurisdictional loops such as:
- municipal → judicial → municipal
- federal → municipal → federal

This operator is procedural, not interpretive.
"""

class HolonomyOperator:
    def __init__(self, grammar):
        self.grammar = grammar

    def find_loops(self):
        """
        Identify cycles in the node-edge graph.
        Returns a list of loops, each represented as a list of node IDs.
        """
        loops = []
        visited = set()

        def dfs(node, path):
            if node in path:
                loops.append(path[path.index(node):] + [node])
                return
            for edge in self.grammar["edges"]:
                if edge["from"] == node:
                    dfs(edge["to"], path + [node])

        for n in self.grammar["nodes"]:
            dfs(n["id"], [])

        return loops
