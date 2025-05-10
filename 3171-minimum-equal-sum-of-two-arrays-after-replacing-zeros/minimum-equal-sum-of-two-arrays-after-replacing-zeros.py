from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Replaces all 0s in both lists with 1s, then returns the maximum of the two sums.
        If either original list has no zeros and its sum is less than the other's adjusted sum, return -1.
        """

        has_zero1 = 0 in nums1
        has_zero2 = 0 in nums2

        sum1 = sum(num if num != 0 else 1 for num in nums1)
        sum2 = sum(num if num != 0 else 1 for num in nums2)

        if not has_zero1 and sum(nums1) < sum2:
            return -1
        if not has_zero2 and sum(nums2) < sum1:
            return -1

        return max(sum1, sum2)
