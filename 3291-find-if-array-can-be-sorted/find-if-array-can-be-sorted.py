from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # Helper function to count '1' bits in the binary representation of a number
        def count_ones_in_binary(num):
            return bin(num).count("1")

        # Dictionary to store the bit count for each unique number in nums
        bit_count_map = {num: count_ones_in_binary(num) for num in set(nums)}

        # List to track min and max values in each contiguous group with the same bit count
        min_max_groups = []
        current_bit_count = bit_count_map[nums[0]]
        current_min, current_max = nums[0], nums[0]

        # Iterate through nums to form groups based on bit counts
        for num in nums:
            # Update min and max for the current group if bit count is the same
            if bit_count_map[num] == current_bit_count:
                current_min = min(current_min, num)
                current_max = max(current_max, num)
            else:
                # Append min and max of completed group and start a new group
                min_max_groups.extend([current_min, current_max])
                current_bit_count = bit_count_map[num]
                current_min, current_max = num, num

        # Append the min and max of the last group
        min_max_groups.extend([current_min, current_max])

        # Check if the min-max pairs are sorted to confirm if array can be sorted by group swaps
        return min_max_groups == sorted(min_max_groups)
