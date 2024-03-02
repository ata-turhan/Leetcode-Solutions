class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        i, j = 0, n - 1
        for k in range(n - 1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                res[k] = nums[i] ** 2
                i += 1
            else:
                res[k] = nums[j] ** 2
                j -= 1
        return res
        