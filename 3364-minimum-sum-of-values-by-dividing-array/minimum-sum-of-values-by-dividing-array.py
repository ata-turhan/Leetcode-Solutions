from functools import cache
from math import inf
from typing import List

class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        # Get the lengths of nums and andValues
        m, n = len(nums), len(andValues)
        
        # Define the recursive function with memoization
        @cache
        def fn(i, j, mask): 
            """Return min sum at nums[j] and andValues[k] with given mask."""
            # Base case: if we reach the end of both nums and andValues, return 0
            if i == m and j == n:
                return 0
            # Base case: if we reach the end of either nums or andValues, return infinity
            if i == m or j == n:
                return inf 
            
            # Update the mask with the bitwise AND of nums[i]
            mask &= nums[i]
            
            # If the updated mask is less than andValues[j], return infinity
            if mask < andValues[j]:
                return inf 
            
            # If the updated mask equals andValues[j], recursively call fn with two options:
            # 1. Exclude nums[i] from the current subarray
            # 2. Include nums[i] in the current subarray
            if mask == andValues[j]:
                return min(fn(i + 1, j, mask), nums[i] + fn(i + 1, j + 1, -1))
            
            # If the updated mask is greater than andValues[j], exclude nums[i] from the current subarray
            return fn(i + 1, j, mask)
            
        # Call fn to find the minimum possible sum of subarrays
        ans = fn(0, 0, -1)
        
        # If it's not possible to divide the array according to the given conditions, return -1
        return ans if ans < inf else -1
