class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row: int, col: int) -> None:
            if (
                row < 0
                or col < 0
                or row >= len(grid)
                or col >= len(grid[0])
                or grid[row][col] == '0'
            ):
                return

            grid[row][col] = '0'

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        island_num = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    island_num += 1
                    dfs(row, col)

        return island_num