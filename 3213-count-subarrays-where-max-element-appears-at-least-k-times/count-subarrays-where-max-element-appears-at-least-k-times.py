from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_el = max(nums)
        res = 0
        max_idx = []
        for i, num in enumerate(nums):
            if num == max_el:
                max_idx.append(i)
            if len(max_idx) >= k:
                res += max_idx[-k] + 1
        return res
