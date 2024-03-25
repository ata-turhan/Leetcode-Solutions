# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        # Initialize left and right pointers for binary search.
        left = 0
        right = 2**31  # Use 2^31 as an upper bound for binary search.
        
        while left <= right:
            # Calculate the middle index.
            mid = left + (right - left) // 2
            
            # Get the value at the middle index from the ArrayReader.
            result = reader.get(mid)
            
            if result == target:
                # If the target is found, return the index.
                return mid
            elif result == 2**31 - 1 or result > target:
                # If the value at mid is greater than the target or it's the upper bound,
                # adjust the right pointer.
                right = mid - 1
            else:
                # If the value at mid is less than the target, adjust the left pointer.
                left = mid + 1
        
        # If the target is not found, return -1.
        return -1
