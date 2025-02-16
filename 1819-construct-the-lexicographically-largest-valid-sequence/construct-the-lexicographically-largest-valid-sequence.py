from typing import List

class Solution: 
    def constructDistancedSequence(self, n: int) -> List[int]:
        # The length of the sequence must be 2*n - 1
        length = 2 * n - 1
        sequence = [-1] * length
        used = [False] * (n + 1)  # used[i] is True if i is already placed
        
        # Define the backtracking function
        def backtrack(index: int) -> bool:
            # If we have filled the sequence, return True
            if index == length:
                return True
            # If this index is already filled, skip to the next index
            if sequence[index] != -1:
                return backtrack(index + 1)
            
            # Try placing numbers from n down to 1 (for lexicographically largest order)
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                # For num == 1, we only need one position
                if num == 1:
                    sequence[index] = 1
                    used[1] = True
                    if backtrack(index + 1):
                        return True
                    # Backtrack
                    sequence[index] = -1
                    used[1] = False
                else:
                    # For numbers greater than 1, the second occurrence must be exactly num indices apart
                    next_index = index + num
                    if next_index < length and sequence[next_index] == -1:
                        sequence[index] = num
                        sequence[next_index] = num
                        used[num] = True
                        if backtrack(index + 1):
                            return True
                        # Backtrack: Remove the placements
                        sequence[index] = -1
                        sequence[next_index] = -1
                        used[num] = False
            return False

        backtrack(0)
        return sequence
