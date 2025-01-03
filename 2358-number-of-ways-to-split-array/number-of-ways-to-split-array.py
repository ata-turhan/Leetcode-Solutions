class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        half_sum = sum(nums) / 2
        valid_split_count = 0
        cum_sum = 0
        for i in range(len(nums) - 1):
            cum_sum += nums[i]
            if cum_sum >= half_sum:
                valid_split_count += 1

        return valid_split_count
        