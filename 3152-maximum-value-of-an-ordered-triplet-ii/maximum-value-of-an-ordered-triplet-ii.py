from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        Computes the maximum value of the expression:
        (nums[i] - nums[j]) * nums[k] for i < j < k,
        using prefix and suffix maximum arrays.
        """

        n = len(nums)
        prefix_max: List[int] = [0] * n
        suffix_max: List[int] = [0] * n

        # Build prefix max array: max value before index i
        current_max = 0
        for i in range(n):
            prefix_max[i] = current_max
            current_max = max(current_max, nums[i])

        # Build suffix max array: max value after index i
        current_max = 0
        for i in range(n - 1, -1, -1):
            suffix_max[i] = current_max
            current_max = max(current_max, nums[i])

        # Evaluate maximum triplet value using prefix and suffix
        max_triplet_value = 0
        for i in range(n):
            diff = prefix_max[i] - nums[i]
            if diff > 0:
                triplet_value = diff * suffix_max[i]
                max_triplet_value = max(max_triplet_value, triplet_value)

        return max_triplet_value
