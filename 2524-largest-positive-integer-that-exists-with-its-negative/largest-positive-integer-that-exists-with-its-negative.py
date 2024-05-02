class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        set_nums = set(nums)
        res = -1
        for num in nums:
            if num > 0 and -num in set_nums:
                res = max(res, num)
        return res