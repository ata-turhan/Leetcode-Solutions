class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize the TicTacToe board of size n.
        """
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.antidiagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at (row, col).
        @param row: The row of the board.
        @param col: The column of the board.
        @param player: The player, either 1 or 2.
        @return: The current winning condition, either 0, 1, or 2.
        """
        # Determine the value to add (1 for player 1, -1 for player 2)
        value = 1 if player == 1 else -1
        win_value = value * self.n

        # Update the row count
        self.rows[row] += value
        if self.rows[row] == win_value:
            return player

        # Update the column count
        self.cols[col] += value
        if self.cols[col] == win_value:
            return player

        # Update the diagonal count if applicable
        if row == col:
            self.diagonal += value
            if self.diagonal == win_value:
                return player

        # Update the antidiagonal count if applicable
        if row + col == self.n - 1:
            self.antidiagonal += value
            if self.antidiagonal == win_value:
                return player

        # No winner yet
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row, col, player)
