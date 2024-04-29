class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = reduce(lambda a, b:a^b, nums)
        res = total ^ k
        count = 0
        while res > 0:
            res &= res-1
            count += 1
        return count
        