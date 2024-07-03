from typing import List
import heapq

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums_size = len(nums)
        
        # If there are 4 or fewer elements, we can make the array equal
        if nums_size <= 4:
            return 0
        
        # Find the smallest four elements
        smallest_four = sorted(heapq.nsmallest(4, nums))
        
        # Find the largest four elements
        largest_four = sorted(heapq.nlargest(4, nums))
        
        min_diff = float("inf")
        
        # Compare the differences between the largest and smallest elements
        for i in range(4):
            min_diff = min(min_diff, largest_four[i] - smallest_four[i])
        
        return min_diff
