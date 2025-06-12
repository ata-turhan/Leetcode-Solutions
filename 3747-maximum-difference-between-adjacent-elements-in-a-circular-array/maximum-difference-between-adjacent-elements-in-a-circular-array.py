class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_dist = abs(nums[0] - nums[-1])

        for i in range(len(nums) - 1):
            max_dist = max(max_dist, abs(nums[i + 1] - nums[i]))

        return max_dist
        