from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        """
        Partitions the array into the minimum number of subsequences
        such that the absolute difference between the minimum and 
        maximum of each subsequence is less than or equal to k.
        """
        nums.sort()
        subsequence_count = 1
        subsequence_min = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > subsequence_min + k:
                subsequence_count += 1
                subsequence_min = nums[i]

        return subsequence_count
