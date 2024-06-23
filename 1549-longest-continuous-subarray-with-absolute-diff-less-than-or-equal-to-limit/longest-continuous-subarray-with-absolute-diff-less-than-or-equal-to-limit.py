from sortedcontainers import SortedList

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        max_len = 0
        window = SortedList()
        for r in range(len(nums)):
            window.add(nums[r])
            diff = window[-1] - window[0]
            if diff <= limit:
                max_len = max(max_len, len(window))
            else:
                window.remove(nums[l])
                l += 1
        return max_len

        