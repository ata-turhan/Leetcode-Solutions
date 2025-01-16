class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor_nums1 = 0 if len(nums2) % 2 == 0 else reduce(lambda a, b: a ^ b, nums1)
        xor_nums2 = 0 if len(nums1) % 2 == 0 else reduce(lambda a, b: a ^ b, nums2)
        return xor_nums1 ^ xor_nums2
        