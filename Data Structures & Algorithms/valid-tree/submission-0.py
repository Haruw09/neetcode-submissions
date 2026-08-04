from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)
        for node_1, node_2 in edges:
            graph[node_1].append(node_2)
            graph[node_2].append(node_1)

        visited = set()
        def dfs(node: int) -> None:
            if node in visited:
                return

            visited.add(node)
            for next_node in graph[node]:
                dfs(next_node)

        dfs(0)
        return len(visited) == n
        