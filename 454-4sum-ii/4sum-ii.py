class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        first_sums = defaultdict(int)
        for num1 in nums1:
            for num2 in nums2:
                first_sums[num1 + num2] += 1
        
        res = 0
        for num3 in nums3:
            for num4 in nums4:
                if -(num3 + num4) in first_sums:
                    res += first_sums[-(num3 + num4)]
        return res