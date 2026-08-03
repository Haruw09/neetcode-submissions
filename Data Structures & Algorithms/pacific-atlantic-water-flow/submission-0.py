from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for row in range(rows):
            pacific.add((row, 0))
            atlantic.add((row, cols - 1))

        for col in range(cols):
            pacific.add((0, col))
            atlantic.add((rows - 1, col))

        def bfs(dots: set) -> set:
            cur = deque(dots)
            while cur:
                cur_row, cur_col = cur.popleft()
                for direction in directions:
                    new_row = cur_row + direction[0]
                    new_col = cur_col + direction[1]
                    if (
                        (new_row, new_col) not in dots
                        and 0 <= new_row < rows
                        and 0 <= new_col < cols
                        and heights[new_row][new_col] >= heights[cur_row][cur_col]
                    ):
                        cur.append((new_row, new_col))
                        dots.add((new_row, new_col))

            return dots
        return [[row, col] for row, col in bfs(pacific) & bfs(atlantic)]
