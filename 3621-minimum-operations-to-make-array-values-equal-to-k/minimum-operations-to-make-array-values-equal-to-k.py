from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Counts how many unique numbers in the list are strictly greater than k.
        If any number in nums is less than k, return -1.
        """
        if any(num < k for num in nums):
            return -1
        
        unique_greater_than_k = sum(1 for num in set(nums) if num > k)
        return unique_greater_than_k
