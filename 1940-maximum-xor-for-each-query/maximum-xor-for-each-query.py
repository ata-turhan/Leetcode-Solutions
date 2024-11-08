class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        total_xor = reduce(lambda a, b: a ^ b, nums)
        queries = []

        for i in range(len(nums)-1, -1, -1):
            k = 0
            for j in range(maximumBit):
                k |= (((total_xor >> j) & 1) ^ 1) << j
            queries.append(k)

            total_xor ^= nums[i]

        return queries
        