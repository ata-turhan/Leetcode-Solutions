from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Use XOR operation to find the single number that appears only once
        return reduce(lambda a, b: a ^ b, nums)
