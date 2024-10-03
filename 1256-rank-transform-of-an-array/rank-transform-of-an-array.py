from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        # Remove duplicates and sort the array to get unique elements in ascending order
        sorted_arr = sorted(set(arr))

        # Create a dictionary that maps each number to its rank
        ranks = {num: rank for rank, num in enumerate(sorted_arr, start=1)}

        # Map each number in the original array to its corresponding rank
        return [ranks[num] for num in arr]
