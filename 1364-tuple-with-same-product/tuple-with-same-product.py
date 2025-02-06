from math import factorial

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        multiplications = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                multiplication = nums[i] * nums[j]
                multiplications[multiplication] += 1

        total_tuples = 0
        for value in multiplications.values():
            if value >= 2:
                total_tuples += factorial(value) / factorial(value - 2) * 4

        return int(total_tuples)