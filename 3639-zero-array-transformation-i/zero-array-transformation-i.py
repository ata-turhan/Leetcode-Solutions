class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        decrements = [0] * n
        for l, r in queries:
            decrements[l] += 1
            if r < n - 1:
                decrements[r + 1] -= 1

        for i in range(1, n):
            decrements[i] += decrements[i - 1]

        for i in range(n):
            if decrements[i] < nums[i]:
                return False

        return True
        