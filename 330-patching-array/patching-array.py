class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        index = 0
        missing_number = 1  # Initialize missing_number to track the smallest missing number

        while missing_number <= n:
            if index < len(nums) and nums[index] <= missing_number:  # Check if current number can cover the missing number
                missing_number += nums[index]  # Update missing_number to the next missing number
                index += 1  # Move to the next number in nums
            else:  # If the current number can't cover the missing number, patch the array
                missing_number += missing_number  # Double the missing_number
                patches += 1  # Increment the patch count

        return patches  # Return the total number of patches
