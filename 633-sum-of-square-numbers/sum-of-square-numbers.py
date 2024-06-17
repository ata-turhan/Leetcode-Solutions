class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def binary_search(start: int, end: int, target: int) -> bool:
            while start <= end:
                mid = start + (end - start) // 2  # Calculate the midpoint to avoid overflow.
                if mid * mid == target:
                    return True  # Found the number whose square equals the target.
                elif mid * mid > target:
                    end = mid - 1  # Search in the left half.
                else:
                    start = mid + 1  # Search in the right half.
            return False

        a = 0
        while a * a <= c:
            b = c - a * a  # Calculate the remaining value to find its square root.
            if binary_search(0, b, b):
                return True  # Found a pair (a, b) such that a^2 + b^2 = c.
            a += 1
        return False  # No such pair exists.
