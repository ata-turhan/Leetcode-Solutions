from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        """Applies operations on the array and shifts non-zero elements to the left."""
        n = len(nums)

        # Step 1: Apply operations (merge adjacent equal numbers)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # Step 2: Shift non-zero elements to the left
        res = [num for num in nums if num != 0]
        res.extend([0] * (n - len(res)))  # Append zeros to maintain original length

        return res
