class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 3:
            return False
        num = 3
        while num <= n:
            if num == n:
                return True
            num **= 2
        num = num**0.5
        while num <= n:
            if num == n:
                return True
            num *= 3
        return False