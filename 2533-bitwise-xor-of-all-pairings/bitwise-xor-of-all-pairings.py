from functools import reduce
from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Compute the XOR of all pairs formed by taking one element from nums1 and one from nums2.

        :param nums1: List[int] - The first list of integers.
        :param nums2: List[int] - The second list of integers.
        :return: int - The XOR of all pairs (nums1[i] XOR nums2[j]).
        """
        # If nums2 has an odd number of elements, every element in nums1 will contribute to the result.
        xor_from_nums1 = 0 if len(nums2) % 2 == 0 else reduce(lambda a, b: a ^ b, nums1)

        # If nums1 has an odd number of elements, every element in nums2 will contribute to the result.
        xor_from_nums2 = 0 if len(nums1) % 2 == 0 else reduce(lambda a, b: a ^ b, nums2)

        # The result is the XOR of contributions from both nums1 and nums2.
        return xor_from_nums1 ^ xor_from_nums2
