class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        size = [1] * (len(edges) + 1)
        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])
                node = parent[node]
            return node

        def union(node_1: int, node_2: int) -> bool:
            head_1 = find(node_1)
            head_2 = find(node_2)
            if head_1 == head_2:
                return False

            if size[head_1] < size[head_2]:
                head_1, head_2 = head_2, head_1

            parent[head_2] = parent[head_1]
            size[head_1] += size[head_2]
            return True

        result = []
        for node_1, node_2 in edges:
            if not union(node_1, node_2):
                result = [node_1, node_2]

        return result
