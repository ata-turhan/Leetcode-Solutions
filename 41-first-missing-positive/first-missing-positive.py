from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # Ensure nums[i] is within the range [1, n] and not already in its correct position
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # Swap nums[i] with the element at index nums[i] - 1
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Iterate through nums to find the smallest missing positive integer
        for j in range(n):
            if nums[j] != j + 1:
                return j + 1
        
        # If all elements are at their correct positions, the smallest missing positive number is n + 1
        return n + 1
