class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Check if the sequence of 'L' and 'R' pieces is identical in order
        if [char for char in start if char != "_"] != [char for char in target if char != "_"]:
            return False

        idx_start = 0
        for i in range(len(target)):
            if target[i] == "_":
                continue
            elif target[i] == "L":
                while idx_start < len(start) and start[idx_start] != "L":
                    idx_start += 1
                # Check if 'L' in start is misplaced
                if idx_start == len(start) or idx_start < i:
                    return False
                idx_start += 1  # Move past the matched 'L'
            elif target[i] == "R":
                while idx_start < len(start) and start[idx_start] != "R":
                    idx_start += 1
                # Check if 'R' in start is misplaced
                if idx_start == len(start) or idx_start > i:
                    return False
                idx_start += 1  # Move past the matched 'R'

        return True
