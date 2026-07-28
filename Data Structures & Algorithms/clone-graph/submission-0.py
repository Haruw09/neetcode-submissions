"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        copies = dict()
        def clone(node: Node | list) -> Node | None:
            if not node:
                return None
            
            new_node = Node(node.val)
            copies[node] = new_node

            for nei in node.neighbors:
                if nei not in copies:
                    copies[nei] = clone(nei)

                new_node.neighbors.append(copies[nei])
            
            return new_node

        return clone(node)