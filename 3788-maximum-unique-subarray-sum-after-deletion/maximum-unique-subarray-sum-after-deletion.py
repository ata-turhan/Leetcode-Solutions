class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if len([num for num in nums if num >= 0]):
            return sum(set(num for num in nums if num >= 0))
        else:
            return max(nums)
        