class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        max_area = 0

        def find_island(row: int, col: int) -> int:
            if grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            area = 1

            for direction in directions:
                new_row = direction[0] + row
                new_col = direction[1] + col
                if (
                    0 <= new_row < len(grid)
                    and 0 <= new_col < len(grid[0])
                ):
                    area += find_island(new_row, new_col)

            return area

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(find_island(row, col), max_area)

        return max_area
