from collections import defaultdict
from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        """
        Processes a sequence of queries where each query assigns a color to a specific ball.
        Tracks the number of distinct colors present in the system after each query.

        :param limit: Upper bound on the number of balls.
        :param queries: List of queries where each query contains [ball_index, color].
        :return: List of integers representing the number of distinct colors after each query.
        """
        ball_to_color = defaultdict(lambda: -1)  # Maps each ball to its assigned color
        color_frequency = defaultdict(int)  # Tracks the count of each color
        result = []
        distinct_color_count = 0  # Number of distinct colors present

        for ball_index, color in queries:
            # If the ball already has a color, decrement the frequency of the previous color
            if ball_to_color[ball_index] != -1:
                previous_color = ball_to_color[ball_index]
                color_frequency[previous_color] -= 1

                # If the previous color is no longer used, decrement distinct color count
                if color_frequency[previous_color] == 0:
                    distinct_color_count -= 1
            
            # Assign the new color to the ball
            ball_to_color[ball_index] = color
            color_frequency[color] += 1

            # If this color is assigned for the first time, increment distinct color count
            if color_frequency[color] == 1:
                distinct_color_count += 1

            # Append the current count of distinct colors
            result.append(distinct_color_count)

        return result
