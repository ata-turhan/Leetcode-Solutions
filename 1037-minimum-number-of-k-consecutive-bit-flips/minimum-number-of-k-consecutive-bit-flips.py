from collections import deque
from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        queue = deque()
        count = 0

        for i in range(n):
            if queue and queue[0] == i:
                queue.popleft()

            if (len(queue) % 2 == 0 and nums[i] == 0) or (len(queue) % 2 == 1 and nums[i] == 1):
                if i + k > n:
                    return -1
                queue.append(i + k)
                count += 1

        return count
