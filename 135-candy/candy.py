from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Initialize candies array with 1 candy for each child
        candies_distribution = [1] * len(ratings)

        # First pass: left to right to satisfy increasing rating condition
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies_distribution[i] = candies_distribution[i - 1] + 1

        # Second pass: right to left to satisfy decreasing rating condition
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies_distribution[i] = max(candies_distribution[i], candies_distribution[i + 1] + 1)

        # Total candies required is the sum of the distribution array
        return sum(candies_distribution)
