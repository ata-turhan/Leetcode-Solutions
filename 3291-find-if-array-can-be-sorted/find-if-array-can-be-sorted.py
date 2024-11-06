from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # Function to get the count of '1' bits in the binary representation of a number
        def count_bits(num):
            return bin(num).count("1")

        # Cache bit counts for each unique number in nums
        bit_counts = {num: count_bits(num) for num in set(nums)}

        # Create groups of numbers based on their bit counts, tracking min and max in each group
        groups = []
        current_bit_count = bit_counts[nums[0]]
        min_num, max_num = nums[0], nums[0]

        for num in nums:
            # If current num has the same bit count as previous, update min and max in the current group
            if bit_counts[num] == current_bit_count:
                min_num = min(min_num, num)
                max_num = max(max_num, num)
            else:
                # Append min and max of the finished group and reset for new group
                groups.extend([min_num, max_num])
                current_bit_count = bit_counts[num]
                min_num, max_num = num, num

        # Append the min and max of the last group
        groups.extend([min_num, max_num])

        # Check if the groups' min-max values are sorted, indicating array can be sorted with swaps
        return groups == sorted(groups)
