from typing import List
from collections import Counter

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        Finds a special integer x such that there are exactly x numbers in the array
        that are greater than or equal to x. If no such integer exists, returns -1.
        
        :param nums: List[int] - List of integers.
        :return: int - The special integer x or -1 if no such integer exists.
        """

        # Create a frequency counter for elements in nums
        freq_counter = Counter(nums)

        # Convert the counter to a sorted list of tuples (element, frequency)
        # sorted in descending order based on the elements
        freq_items = sorted(freq_counter.items(), reverse=True)
        
        # Initialize the count of elements seen so far
        count = 0
        prev_val = -1
        
        # Iterate over each unique element and its frequency in descending order
        for value, freq in freq_items:
            # Check if the current value is less than the count and the count
            # is less than or equal to the previous value
            if value < count <= prev_val:
                return count  # Found the special integer

            # Accumulate the total number of elements considered so far
            count += freq

            # Update the previous value to the current value
            prev_val = value
        
        # After the loop, check if the total count is a valid special number
        # The count should be less than or equal to the smallest number in nums
        return count if count <= min(nums) else -1

# Example usage:
# sol = Solution()
# print(sol.specialArray([3, 5, 0, 3, 4]))  # Output example: 3
