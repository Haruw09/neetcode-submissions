class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        size = [1] * n
        comps = n

        def find(node: int) -> int:
            i = node
            while parent[i] != i:
                i = parent[i]

            return i

        def union(node_1: int, node_2: int) -> bool:
            head_1 = find(node_1)
            head_2 = find(node_2)

            if head_1 == head_2:
                return False

            if size[head_1] < size[head_2]:
                head_1, head_2 = head_2, head_1

            parent[head_2] = head_1
            size[head_1] += size[head_2]

            return True


        for node_1, node_2 in edges:
            if union(node_1, node_2):
                comps -= 1
            else:
                return False

        return True if comps == 1 else False
            