from typing import List
from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        """
        Finds all unique 3-digit even numbers that can be formed using digits from the input list.
        Each digit can be used at most once in a number.
        """
        valid_numbers = set()

        for perm in permutations(digits, 3):
            if perm[0] != 0 and perm[2] % 2 == 0:
                number = perm[0] * 100 + perm[1] * 10 + perm[2]
                valid_numbers.add(number)

        return sorted(valid_numbers)
