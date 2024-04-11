from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Compute the intersection of nums1 and nums2 using Counter objects
        intersection = Counter(nums1) & Counter(nums2)
        # Construct a list containing elements from the intersection along with their multiplicities
        return [key for key in intersection for _ in range(intersection[key])]
