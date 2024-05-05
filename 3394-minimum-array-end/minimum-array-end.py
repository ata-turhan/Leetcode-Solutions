class Solution:
    def minEnd(self, n: int, x: int) -> int:
        num = x
        bit = 1  
        n -= 1
        while n > 0:
            if (x & bit) == 0:
                num |= (n & 1) * bit
                n >>= 1
            bit <<= 1
        return num