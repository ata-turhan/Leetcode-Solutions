class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_live_neighbors(row, col, rows, cols):
            directions = [
                (0, 1), (1, 0), (1, 1), (0, -1), 
                (-1, 0), (-1, -1), (1, -1), (-1, 1)
            ]
            live_count = 0
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] in (1, -2):
                    live_count += 1
            return live_count

        rows = len(board)
        cols = len(board[0])

        # First pass to mark the board with transitional states
        for row in range(rows):
            for col in range(cols):
                live_neighbors = get_live_neighbors(row, col, rows, cols)
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -2  # Live cell that will die
                elif board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = -1  # Dead cell that will become live

        # Second pass to finalize the board state
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == -2:
                    board[row][col] = 0
                elif board[row][col] == -1:
                    board[row][col] = 1
