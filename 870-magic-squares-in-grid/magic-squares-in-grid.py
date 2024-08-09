class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # Define the set of numbers needed for a 3x3 magic square
        required_set = Counter([1, 2, 3, 4, 5, 6, 7, 8, 9])
        
        def isMagicSquare(r: int, c: int) -> bool:
            # Extract the 3x3 grid values
            nums = [grid[r + i][c + j] for i in range(3) for j in range(3)]
            # Check if the numbers are exactly 1 through 9
            if Counter(nums) != required_set:
                return False

            # Calculate sums of rows, columns, and diagonals
            rows = [sum(grid[r + i][c + j] for j in range(3)) for i in range(3)]
            cols = [sum(grid[r + i][c + j] for i in range(3)) for j in range(3)]
            diagonal1 = sum(grid[r + i][c + i] for i in range(3))
            diagonal2 = sum(grid[r + i][c + 2 - i] for i in range(3))

            # Collect all sums
            all_sums = rows + cols + [diagonal1, diagonal2]
            
            # A 3x3 magic square has equal sums in all rows, columns, and diagonals
            return len(set(all_sums)) == 1

        m, n = len(grid), len(grid[0])
        magic_count = 0

        # Iterate over all possible top-left corners of 3x3 sub-grids
        for i in range(m - 2):
            for j in range(n - 2):
                if isMagicSquare(i, j):
                    magic_count += 1

        return magic_count
