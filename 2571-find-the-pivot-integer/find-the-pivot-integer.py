class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = list(range(1, n+1))
        total_sum = sum(nums)
        left_sum = 0

        for num in nums:
            total_sum -= num

            if left_sum == total_sum:
                return num

            left_sum += num

        return -1