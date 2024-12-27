from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        Calculate the maximum score of a sightseeing pair.
        
        The score of a pair (i, j) is values[i] + values[j] + i - j.
        
        :param values: List of integer values representing points of interest.
        :return: Maximum score of a sightseeing pair.
        """
        # `best_prev` keeps track of the best value of values[i] + i so far
        best_prev = values[0]
        max_score = 0

        # Start iterating from the second element (index 1)
        for j in range(1, len(values)):
            # Calculate the score for the current pair (best_prev, values[j])
            max_score = max(max_score, best_prev + values[j] - j)
            
            # Update the best value of values[i] + i for future pairs
            best_prev = max(best_prev, values[j] + j)

        return max_score
