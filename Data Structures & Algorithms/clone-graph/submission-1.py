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
        def clone(node: Node | None) -> Node | None:
            if node in copies:
                return copies[node]
            
            new_node = Node(node.val)
            copies[node] = new_node

            for nei in node.neighbors:
                new_node.neighbors.append(clone(nei))
            
            return new_node

        return clone(node)