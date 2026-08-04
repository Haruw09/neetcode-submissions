class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1] * n
        comps = n

        def find(node: int) -> int:
            i = node
            while i != parent[i]:
                i = parent[i]

            return i

        def union(node_1: int, node_2: int) -> bool:
            root_1 = find(node_1)
            root_2 = find(node_2)

            if root_1 == root_2:
                return False

            if size[root_1] < size[root_2]:
                root_1, root_2 = root_2, root_1

            parent[root_2] = root_1
            size[root_1] += size[root_2]

            return True

        for node_1, node_2 in edges:
            if union(node_1, node_2):
                comps -= 1
            
        return comps