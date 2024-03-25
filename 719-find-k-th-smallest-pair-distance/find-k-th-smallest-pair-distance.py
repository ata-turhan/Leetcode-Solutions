class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Sort the input list of numbers.
        nums.sort()
        n = len(nums)
        
        # Initialize the search range.
        low, high = 0, nums[-1] - nums[0]
        
        # Perform binary search on the range of possible distances.
        while low <= high:
            mid = (low + high) // 2
            count = 0
            j = 0
            # Count the number of pairs with a distance less than or equal to mid.
            for i in range(n):
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1
            if count < k:
                # If the count is less than k, adjust the lower bound of the search range.
                low = mid + 1
            else:
                # If the count is greater than or equal to k, adjust the upper bound of the search range.
                high = mid - 1
        
        # Return the smallest distance found.
        return low

        