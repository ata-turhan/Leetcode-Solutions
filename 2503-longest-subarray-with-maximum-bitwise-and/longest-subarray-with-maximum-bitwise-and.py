class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        longest = 0
        count = 0
        for num in nums:
            if num != max_val:
                count = 0
            else:
                count += 1
                longest = max(longest, count)

        return longest
        