class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        if n == 1:
            return 0  # Base case: only one child, no rotations needed

        cycles = k // (n - 1)  # Determine the number of complete cycles
        position = k % (n - 1)  # Determine the position within the current cycle

        if cycles % 2 == 0:
            return position  # If the number of cycles is even, return the position directly
        else:
            return n - 1 - position  # If the number of cycles is odd, return the mirrored position
