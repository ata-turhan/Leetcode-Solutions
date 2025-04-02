class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_value_after = [0] * len(nums)
        max_val = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            max_value_after[i] = max_val
            max_val = max(max_val, nums[i])

        max_triplet_val = float("-inf")

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                val = (nums[i] - nums[j]) * max_value_after[j]
                max_triplet_val = max(max_triplet_val, val)

        return max_triplet_val if max_triplet_val > 0 else 0        