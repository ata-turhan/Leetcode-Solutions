from collections import deque
from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        queue = deque()
        flip_count = 0

        for i in range(n):
            # Remove the index from the front of the queue if it is out of the current window
            if queue and queue[0] == i:
                queue.popleft()

            # Determine the current bit state after flips
            current_state = nums[i] if len(queue) % 2 == 0 else 1 - nums[i]

            # If the current bit needs to be flipped
            if current_state == 0:
                # If flipping would go beyond the array, return -1
                if i + k > n:
                    return -1
                # Add the index where the current flip window ends
                queue.append(i + k)
                flip_count += 1

        return flip_count
