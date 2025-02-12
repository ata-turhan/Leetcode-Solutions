class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def calc_sum_digits(num):
            res = 0
            while num > 0:
                res += num % 10
                num //= 10

            return res

        sum_digits = defaultdict(list)

        for num in nums:
            sum_ = calc_sum_digits(num)
            heappush(sum_digits[sum_], -num)

        max_sum = -1

        for heap in sum_digits.values():
            if len(heap) >= 2:
                max_val, second_max_val = -heappop(heap), -heappop(heap)
                max_sum = max(max_sum, max_val + second_max_val)

        return max_sum
        