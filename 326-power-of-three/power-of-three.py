class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 3:
            return False
        
        num = 3
        # Check if n is a power of 3 by continuously squaring num
        while num <= n:
            if num == n:
                return True
            num *= num
        
        # Check if n is a power of 3 by continuously taking the square root of num
        num = num**0.5
        while num <= n:
            if num == n:
                return True
            num *= 3
        
        return False
