from typing import List
from collections import Counter
from bisect import bisect_left

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        Finds a special integer x such that there are exactly x numbers in the array
        that are greater than or equal to x. If no such integer exists, returns -1.
        
        :param nums: List[int] - List of integers.
        :return: int - The special integer x or -1 if no such integer exists.
        """
        # Sort the array to facilitate the counting process
        nums.sort()

        # Create a frequency counter for elements in nums
        freq_counter = Counter(nums)

        # Convert the counter to a sorted list of tuples (element, frequency)
        # sorted in descending order based on the elements
        freq_items = sorted(freq_counter.items(), reverse=True)
        
        # Initialize the count of elements seen so far
        count = 0
        
        # Iterate over each unique element and its frequency in descending order
        for value, freq in freq_items:
            # Accumulate the total number of elements considered so far
            count += freq

            # Use binary search to find the index where 'count' should be inserted
            # in the sorted list to maintain order
            idx = bisect_left(nums, count)

            # Check if 'count' is the number of elements greater than or equal to 'count'
            if count == len(nums) - idx:
                return count
        
        # If no special integer is found, return -1
        return -1

# Example usage:
# sol = Solution()
# print(sol.specialArray([3, 5, 0, 3, 4]))  # Output example: 3
