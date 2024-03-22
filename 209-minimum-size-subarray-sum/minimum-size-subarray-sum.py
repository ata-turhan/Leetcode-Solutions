class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_len = float("inf")
        sum_val = 0
        for r in range(len(nums)):
            sum_val += nums[r]
            while sum_val >= target:
                min_len = min(min_len, r - l + 1)
                sum_val -= nums[l]
                l += 1
        return min_len if min_len != float("inf") else 0