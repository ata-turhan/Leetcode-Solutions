class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(nums)):
            counts[nums[r]] += 1
            while counts[nums[r]] > k:
                counts[nums[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res    