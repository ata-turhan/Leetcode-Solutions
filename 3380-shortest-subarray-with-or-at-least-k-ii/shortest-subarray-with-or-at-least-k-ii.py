from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def calc_or(bits):
            res = 0
            for i in range(64):
                if bits[i] > 0:  # Check if there's at least one element with the bit set at position i
                    res += 2 ** i
            return res

        bits = [0] * 64
        or_val = 0
        left = 0
        min_len = len(nums) + 1

        for right in range(len(nums)):
            i = 0
            num = nums[right]
            while num > 0:
                pos = num & 1
                if pos:
                    bits[i] += 1
                i += 1
                num >>= 1
            or_val = calc_or(bits)

            while left <= right and or_val >= k:
                min_len = min(min_len, right - left + 1)
                i = 0
                num = nums[left]
                while num > 0:
                    pos = num & 1
                    if pos:
                        bits[i] -= 1
                    i += 1
                    num >>= 1
                or_val = calc_or(bits)
                left += 1

        return -1 if min_len == (len(nums) + 1) else min_len
