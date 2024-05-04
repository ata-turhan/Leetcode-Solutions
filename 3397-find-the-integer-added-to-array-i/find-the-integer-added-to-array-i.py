class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        # Find the minimum value in nums1 and nums2
        min_nums1 = min(nums1)
        min_nums2 = min(nums2)

        # Return the difference between the minimum values
        return min_nums2 - min_nums1
