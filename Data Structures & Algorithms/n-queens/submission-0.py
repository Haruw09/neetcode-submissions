class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chosen_cols = set()
        chosen_diags = set()
        chosen_antidiags = set()

        board = [['.'] * n for _ in range(n)]
        result = []
        def backtrack(row: int) -> None:
            if row == n:
                new_board = []
                for i in range(n):
                    new_board.append(''.join(board[i]))
                result.append(new_board)
                return

            for col in range(n):
                if (
                    col not in chosen_cols
                    and row - col not in chosen_diags
                    and row + col not in chosen_antidiags
                ):
                    board[row][col] = 'Q'
                    chosen_cols.add(col)
                    chosen_diags.add(row - col)
                    chosen_antidiags.add(row + col)

                    backtrack(row + 1)
                    
                    board[row][col] = '.'
                    chosen_cols.remove(col)
                    chosen_diags.remove(row - col)
                    chosen_antidiags.remove(row + col)


        backtrack(0)
        return result

            