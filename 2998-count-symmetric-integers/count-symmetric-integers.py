class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(num):
            n = len(str(num))

            if n % 2 == 1:
                return False

            return sum(map(int, str(num)[:n//2])) == sum(map(int, str(num)[n//2:]))

        count_symmetric_nums = 0
        for num in range(low, high + 1):
            if is_symmetric(num):
                count_symmetric_nums += 1

        return count_symmetric_nums
        