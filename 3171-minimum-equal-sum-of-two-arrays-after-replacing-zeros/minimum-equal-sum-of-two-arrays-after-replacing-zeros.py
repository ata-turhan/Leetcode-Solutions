class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1.count(0) == 0 and sum(nums1) < sum(num if num != 0 else 1 for num in nums2):
            return -1 
        elif nums2.count(0) == 0 and sum(nums2) < sum(num if num != 0 else 1 for num in nums1):
            return -1 

        sum_nums1 = sum(num if num != 0 else 1 for num in nums1)
        sum_nums2 = sum(num if num != 0 else 1 for num in nums2)

        return max(sum_nums1, sum_nums2)
        