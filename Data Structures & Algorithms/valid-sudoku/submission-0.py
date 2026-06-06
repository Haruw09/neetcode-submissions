class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_in_row = [set() for _ in range(9)]
        seen_in_column = [set() for _ in range(9)]
        seen_in_square = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                square_num = 3 * (i // 3) + (j // 3)
                if x == '.':
                    continue
                else:
                    if (
                        x in seen_in_row[i] 
                        or x in seen_in_column[j] 
                        or x in seen_in_square[square_num]
                    ):
                        return False
                    else:
                        seen_in_row[i].add(x)
                        seen_in_column[j].add(x)
                        seen_in_square[square_num].add(x)
        return True
