from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        Calculate the maximum number of chunks the array can be split into such that
        each chunk can be independently sorted to match the sorted version of the array.

        :param arr: List of integers to split into chunks.
        :return: Maximum number of chunks.
        """
        sorted_array = sorted(arr)  # Sorted version of the input array
        value_to_sorted_index = {}  # Map each value to its index in the sorted array
        
        # Build the mapping from value to its index in the sorted array
        for index, value in enumerate(sorted_array):
            value_to_sorted_index[value] = index

        chunks = 0  # Number of valid chunks
        max_index_seen = -1  # The largest index encountered so far

        # Iterate through the input array
        for current_index, value in enumerate(arr):
            current_sorted_index = value_to_sorted_index[value]
            max_index_seen = max(max_index_seen, current_sorted_index)

            # If the maximum index encountered matches the current index,
            # a new chunk can be formed
            if max_index_seen == current_index:
                chunks += 1

        return chunks
