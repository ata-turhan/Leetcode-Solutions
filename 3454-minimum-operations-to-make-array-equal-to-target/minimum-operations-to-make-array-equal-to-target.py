from typing import List

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        # Calculate the difference array between target and nums
        difference = [target[i] - nums[i] for i in range(len(target))]

        operations = 0
        prev_value = 0
        is_negative = difference[0] < 0

        # Iterate through each value in the difference array
        for i in range(len(difference)):
            current_value = difference[i]

            if is_negative:
                # When dealing with negative differences
                operations += max(0, prev_value - current_value)
                # Check if we need to switch from negative to non-negative
                if i < len(difference) - 1 and difference[i + 1] > 0:
                    is_negative = False
                    prev_value = 0
                else:
                    prev_value = current_value
            else:
                # When dealing with non-negative differences
                operations += max(0, current_value - prev_value)
                # Check if we need to switch from non-negative to negative
                if i < len(difference) - 1 and difference[i + 1] < 0:
                    is_negative = True
                    prev_value = 0
                else:
                    prev_value = current_value

        return operations
