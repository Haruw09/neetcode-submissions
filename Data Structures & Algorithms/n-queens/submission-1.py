class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chosen_cols = set()
        chosen_diags = set()
        chosen_antidiags = set()

        board = [['.'] * n for _ in range(n)]
        result = []
        def backtrack(row: int) -> None:
            if row == n:
                result.append([''.join(board[i]) for i in range(n)])
                return

            for col in range(n):
                diagonal = row - col
                anti_diagonal = row + col
                if (
                    col not in chosen_cols
                    and diagonal not in chosen_diags
                    and anti_diagonal not in chosen_antidiags
                ):
                    board[row][col] = 'Q'
                    chosen_cols.add(col)
                    chosen_diags.add(diagonal)
                    chosen_antidiags.add(anti_diagonal)

                    backtrack(row + 1)

                    board[row][col] = '.'
                    chosen_cols.remove(col)
                    chosen_diags.remove(diagonal)
                    chosen_antidiags.remove(anti_diagonal)


        backtrack(0)
        return result

            