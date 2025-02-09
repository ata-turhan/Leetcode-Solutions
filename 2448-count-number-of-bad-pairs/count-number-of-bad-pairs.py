from collections import defaultdict
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
        Counts the number of bad pairs in the given array.
        
        A pair (i, j) is considered good if:
        i - j == nums[i] - nums[j]
        This can be rewritten as:
        (i - nums[i]) == (j - nums[j])
        
        :param nums: List of integers.
        :return: Number of bad pairs in the array.
        """
        index_value_difference = defaultdict(int)  # Stores frequency of (i - nums[i]) values
        good_pair_count = 0
        total_pairs = len(nums) * (len(nums) - 1) // 2  # Total possible (i, j) pairs
        
        # Iterate through the array and count the good pairs
        for index, value in enumerate(nums):
            diff = index - value  # Compute (i - nums[i])
            good_pair_count += index_value_difference[diff]  # Add existing occurrences of the same difference
            index_value_difference[diff] += 1  # Increment the count of this difference
        
        # Bad pairs = Total pairs - Good pairs
        return total_pairs - good_pair_count
