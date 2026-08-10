class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        word_len = len(word)
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        
        def find_word(row: int, col: int, char_idx: int) -> bool:
            if char_idx == word_len - 1:
                return True

            start_char = board[row][col]
            board[row][col] = '#'

            for dx, dy in dirs:
                if (
                    0 <= row + dx < rows
                    and 0 <= col + dy < cols
                    and board[row + dx][col + dy] == word[char_idx + 1]
                    and find_word(row + dx, col + dy, char_idx + 1)
                ):
                    board[row][col] = start_char              
                    return True

            board[row][col] = start_char
            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if find_word(row, col, 0):
                        return True
            
        return False

                