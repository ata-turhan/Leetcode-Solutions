class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Computes the integer square root of a non-negative integer x.
        
        :param x: int - The non-negative integer to compute the square root of.
        :return: int - The integer square root of x.
        """
        if x == 0:
            return 0
        
        # Initial guess
        guess = 1
        
        # Double the guess until it is too large
        while guess * guess <= x:
            if guess * guess == x:
                return guess
            guess *= 2
        
        # Binary search to refine the guess
        low = guess // 2
        high = guess
        
        while low <= high:
            mid = (low + high) // 2
            mid_squared = mid * mid
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return high

# Example usage:
# sol = Solution()
# print(sol.mySqrt(8))  # Output: 2
