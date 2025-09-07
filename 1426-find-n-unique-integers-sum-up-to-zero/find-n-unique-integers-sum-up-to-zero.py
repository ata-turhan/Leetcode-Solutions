from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        # Result container
        result = []
        
        # Generate pairs that cancel each other
        for i in range(1, n // 2 + 1):
            result.append(i)    # positive number
            result.append(-i)   # matching negative number
        
        # If n is odd, add 0 to balance the sum
        if n % 2 == 1:
            result.append(0)
        
        return result
