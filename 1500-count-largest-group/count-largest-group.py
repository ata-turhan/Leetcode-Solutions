class Solution:
    def countLargestGroup(self, n: int) -> int:
        def calc_digit_sum(num):
            digit_sum = 0
            
            while num > 0:
                digit_sum += num % 10
                num //= 10

            return digit_sum

        digit_sum_to_values = defaultdict(list)

        for num in range(1, n + 1):
            digit_sum = calc_digit_sum(num)
            digit_sum_to_values[digit_sum].append(num)

        max_size = max( len(nums) for nums in digit_sum_to_values.values())

        return len( [ nums for nums in digit_sum_to_values.values() if len(nums) == max_size ] )
        