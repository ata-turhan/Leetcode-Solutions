class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Verify if the sequence of 'L' and 'R' in both strings matches in order
        start_pieces = [char for char in start if char != "_"]
        target_pieces = [char for char in target if char != "_"]
        if start_pieces != target_pieces:
            return False

        start_index = 0  # Pointer for the `start` string

        for target_index in range(len(target)):
            if target[target_index] == "_":
                continue
            elif target[target_index] == "L":
                # Move the pointer in `start` until we find 'L'
                while start_index < len(start) and start[start_index] != "L":
                    start_index += 1
                # Ensure 'L' is positioned correctly
                if start_index == len(start) or start_index < target_index:
                    return False
                start_index += 1  # Advance past the matched 'L'
            elif target[target_index] == "R":
                # Move the pointer in `start` until we find 'R'
                while start_index < len(start) and start[start_index] != "R":
                    start_index += 1
                # Ensure 'R' is positioned correctly
                if start_index == len(start) or start_index > target_index:
                    return False
                start_index += 1  # Advance past the matched 'R'

        return True
