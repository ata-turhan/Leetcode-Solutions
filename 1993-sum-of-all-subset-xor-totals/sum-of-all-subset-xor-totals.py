class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(2**n):
            val = 0
            count = 0
            while i > 0:
                if i & 1 == 1:
                    val ^= nums[count]
                count += 1
                i >>= 1
            res += val

        return res
        