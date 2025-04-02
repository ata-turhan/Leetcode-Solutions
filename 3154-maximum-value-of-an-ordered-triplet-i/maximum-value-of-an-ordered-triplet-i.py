from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        Finds the maximum value of the expression:
        (nums[i] - nums[j]) * nums[k] with i < j < k.
        Returns 0 if no such positive value exists.
        """
        n = len(nums)
        max_suffix = [0] * n
        max_val = nums[-1]

        # Precompute maximum values from the right (suffix max)
        for i in range(n - 2, -1, -1):
            max_suffix[i] = max_val
            max_val = max(max_val, nums[i])

        max_triplet_value = 0

        for i in range(n):
            for j in range(i + 1, n - 1):
                diff = nums[i] - nums[j]
                if diff > 0:
                    candidate = diff * max_suffix[j]
                    max_triplet_value = max(max_triplet_value, candidate)

        return max_triplet_value
