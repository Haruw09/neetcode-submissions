from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
        row_num = len(grid)
        col_num = len(grid[0])
        def bfs(row: int, col: int) -> int:
            dots = deque([(row, col)])
            seen = set()
            distance = 0
            while dots:
                level_len = len(dots)
                for _ in range(level_len):
                    cur_row, cur_col = dots.popleft()

                    if (cur_row, cur_col) in seen:
                        continue

                    if grid[cur_row][cur_col] == 0:
                        return distance
                    if grid[cur_row][cur_col] == -1:
                        continue
                    
                    for direction in dirs:
                        new_row = cur_row + direction[0]
                        new_col = cur_col + direction[1]
                        if (
                            (new_row, new_col) not in seen
                            and 0 <= new_row < row_num
                            and 0 <= new_col < col_num
                        ):
                            dots.append((new_row, new_col))
                            seen.add((cur_row, cur_col))
                distance += 1
            return 2147483647

        for row in range(row_num):
            for col in range(col_num):
                if grid[row][col] <= 0:
                    continue
                grid[row][col] = bfs(row, col)
                    
