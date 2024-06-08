class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @cache
        def dp(left, right):
            i = left + n - 1 - right  # Calculate the index for the current multiplier

            if i == m:  # Base case: all multipliers are used
                return 0

            # Calculate the maximum score by either taking the left or the right end
            return max(
                multipliers[i] * nums[left] + dp(left + 1, right),
                multipliers[i] * nums[right] + dp(left, right - 1)
            )

        n, m = len(nums), len(multipliers)
        return dp(0, len(nums) - 1)  # Start with the full range of nums
