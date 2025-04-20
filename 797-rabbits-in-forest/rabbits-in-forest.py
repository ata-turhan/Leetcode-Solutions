from typing import List
from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        """
        Given a list of integers 'answers', where answers[i] is the number
        of other rabbits that share the same color as the i-th rabbit,
        return the minimum total number of rabbits that could be in the forest.
        """
        # Count how many rabbits gave each answer x
        freq: Counter[int] = Counter(answers)
        total_rabbits: int = 0

        # Iterate over each distinct answer value x
        for x, count_x in freq.items():
            # Each color-group size is x + 1 rabbits
            group_size: int = x + 1
            
            # How many complete groups of size (x + 1) we can fill
            full_groups: int = count_x // group_size
            # Remaining rabbits that still need a full group
            remainder: int = count_x % group_size

            # Add rabbits from all full groups
            total_rabbits += full_groups * group_size
            
            # If there's any remainder, they form one extra group of size (x + 1)
            if remainder > 0:
                total_rabbits += group_size

        return total_rabbits
