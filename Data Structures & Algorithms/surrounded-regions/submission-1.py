class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        stack = []
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        for row in range(rows):
            if board[row][0] == 'O':
                stack.append((row, 0))
            if board[row][cols - 1] == 'O':
                stack.append((row, cols - 1))

        for col in range(cols):
            if board[0][col] == 'O':
                stack.append((0, col))
            if board[rows - 1][col] == 'O':
                stack.append((rows - 1, col))

        not_surrounded = set(stack)
        while stack:
            row, col = stack.pop()
            board[row][col] = 'X'
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and board[new_row][new_col] == 'O'
                ):
                    board[new_row][new_col] = 'X'
                    stack.append((new_row, new_col))
                    not_surrounded.add((new_row, new_col))

        for row in range(rows):
            for col in range(cols):
                board[row][col] = 'X'
        
        for row, col in not_surrounded:
            board[row][col] = 'O'