from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        """
        Returns all indices i such that there exists an index j with nums[j] == key
        and |i - j| <= k. The result list is sorted in ascending order.
        
        :param nums: List of integers to search.
        :param key: The target value to find in nums.
        :param k: Maximum allowed distance from any occurrence of key.
        :return: Sorted list of valid indices.
        """
        n = len(nums)
        index_set = set()
        
        for i, value in enumerate(nums):
            if value == key:
                start = max(0, i - k)
                end = min(n, i + k + 1)
                for j in range(start, end):
                    index_set.add(j)
        
        return sorted(index_set)
