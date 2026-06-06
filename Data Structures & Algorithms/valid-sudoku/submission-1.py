class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_in_row = [0] * 9
        seen_in_column = [0] * 9
        seen_in_square = [0] * 9
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                square_num = 3 * (i // 3) + (j // 3)
                if x == '.':
                    continue
                else:
                    x = 1 << int(x)
                    if (
                        x & seen_in_row[i] 
                        or x & seen_in_column[j] 
                        or x & seen_in_square[square_num]
                    ):
                        return False
                    else:
                        seen_in_row[i]|= x
                        seen_in_column[j]|= x
                        seen_in_square[square_num]|= x
        return True
