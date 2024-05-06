from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Initialize the first and second numbers to positive infinity
        first_min = float("inf")
        second_min = float("inf")
        
        # Iterate through the list of numbers
        for num in nums:
            # If the current number is less than the first minimum, update the first minimum
            if num < first_min:
                first_min = num
            # If the current number is greater than the first minimum but less than the second minimum,
            # update the second minimum
            elif num != first_min and num < second_min:
                second_min = num
            # If the current number is greater than both the first and second minimums,
            # then we've found an increasing triplet
            elif num > second_min:
                return True
        
        # If no increasing triplet is found, return False
        return False
