from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        bitwise_and = 0
        max_len = 0

        for right in range(len(nums)):
            while (bitwise_and & nums[right]) != 0:
                bitwise_and ^= nums[left]
                left += 1

            bitwise_and ^= nums[right]
            max_len = max(max_len, right - left + 1)

        return max_len
