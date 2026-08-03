from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        fruits = deque()
        fresh = 0
        for row in range(rows):
            for col in range(cols):
                fruit = grid[row][col]
                if fruit == 1:
                    fresh += 1
                if fruit == 2:
                    fruits.append((row, col))

        time = 0
        while fruits and fresh > 0:
            level_len = len(fruits)
            for _ in range(level_len):
                cur_row, cur_col = fruits.popleft()

                for direction in directions:
                    new_row = cur_row + direction[0]
                    new_col = cur_col + direction[1]

                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and grid[new_row][new_col] == 1                        
                    ):
                        fruits.append((new_row, new_col))
                        grid[new_row][new_col] = 2
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1

        
        