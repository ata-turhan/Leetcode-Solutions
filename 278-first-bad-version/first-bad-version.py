# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Find the first bad version using binary search.
        
        Args:
            n (int): The number of versions.
            
        Returns:
            int: The index of the first bad version.
        """
        # Initialize left and right pointers for binary search
        l, r = 1, n
        
        # Perform binary search until left pointer meets or crosses the right pointer
        while l <= r:
            # Calculate the middle version
            mid = (l + r) // 2
            
            # Check if the middle version is a bad version
            if isBadVersion(mid):
                # If mid is bad, check if the previous version is good
                # If it is, mid is the first bad version; otherwise, continue searching left
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    r = mid - 1
            else:
                # If mid is not bad, continue searching right
                l = mid + 1
