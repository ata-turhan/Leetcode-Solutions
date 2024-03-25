class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Initialize the left and right pointers for binary search.
        left, right = 1, num
        
        # Perform binary search until left pointer exceeds the right pointer.
        while left <= right:
            # Calculate the middle value.
            mid = left + (right - left) // 2
            
            # Check if the square of the middle value equals the given number.
            if mid * mid == num:
                return True
            elif mid * mid < num:
                # If the square of the middle value is less than the given number,
                # adjust the left pointer to search in the right half.
                left = mid + 1
            else:
                # If the square of the middle value is greater than the given number,
                # adjust the right pointer to search in the left half.
                right = mid - 1
        
        # If the loop exits without finding a perfect square, return False.
        return False
