from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # First Solution: Counting Sort
        # Step 1: Count the occurrences of each color (0, 1, 2)
        counts = [0] * 3
        for num in nums:
            counts[num] += 1

        # Step 2: Calculate the running sum for placement indices
        running_sum = 0
        for i in range(len(counts)):
            num = counts[i]
            counts[i] = running_sum
            running_sum += num

        # Step 3: Place each number in its correct position in the original array
        temp = nums.copy()
        for num in temp:
            nums[counts[num]] = num
            counts[num] += 1

        # Second Solution: Dutch National Flag Problem (In-place sort)
        l = -1
        # First pass to place all 0s in the beginning
        for r in range(len(nums)):
            if nums[r] == 0:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]
        
        # Second pass to place all 1s after 0s
        for r in range(len(nums)):
            if nums[r] == 1:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]

# Example usage
# sol = Solution()
# arr = [2, 0, 2, 1, 1, 0]
# sol.sortColors(arr)
# print(arr)  # Output should be [0, 0, 1, 1, 2, 2]
