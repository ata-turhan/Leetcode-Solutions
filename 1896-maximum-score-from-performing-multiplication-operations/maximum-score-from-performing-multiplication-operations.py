class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @cache
        def dp(left, right):
            i = left + n - 1 - right

            if i == m:
                return 0

            return max(
                multipliers[i] * nums[left] + dp(left+1, right),
                multipliers[i] * nums[right] + dp(left, right-1),

            )





        n, m = len(nums), len(multipliers)
        return dp(0, len(nums)-1)
        