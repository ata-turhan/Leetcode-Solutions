from collections import deque
from typing import List

class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]

        # Initialize the queue with base binary strings of length 1
        queue = deque([[0], [1]])
        
        # Iterate to build binary strings of length n
        for _ in range(1, n):
            size = len(queue)
            for _ in range(size):
                current_string = queue.popleft()
                if current_string[-1] == 0:
                    # If the last character is 0, append 1
                    current_string.append(1)
                    queue.append(current_string)
                else:
                    # If the last character is 1, append both 0 and 1
                    new_string1 = current_string.copy()
                    new_string2 = current_string.copy()
                    new_string1.append(0)
                    new_string2.append(1)
                    queue.append(new_string1)
                    queue.append(new_string2)

        # Convert list of integers to strings
        return ["".join(map(str, binary_string)) for binary_string in queue]
