from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Calculates the number of unique sequences that can be formed 
        using the given tiles.
        """

        total_sequences = 0

        # Generate all possible permutations for lengths from 1 to len(tiles)
        for length in range(1, len(tiles) + 1):
            unique_permutations = set(permutations(tiles, length))
            total_sequences += len(unique_permutations)

        return total_sequences
