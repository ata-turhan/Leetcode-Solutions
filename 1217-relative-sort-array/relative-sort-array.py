from typing import List
from collections import defaultdict

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_map = defaultdict(int)
        for num in arr1:
            count_map[num] += 1  # Count occurrences of each number in arr1

        result = []

        # Add numbers from arr2 in the order they appear in arr2
        for num in arr2:
            result.extend([num] * count_map[num])
            count_map.pop(num)

        # Collect remaining numbers not in arr2
        remaining_numbers = []
        for num, count in count_map.items():
            remaining_numbers.extend([num] * count)

        remaining_numbers.sort()  # Sort remaining numbers

        return result + remaining_numbers  # Concatenate result with sorted remaining numbers
