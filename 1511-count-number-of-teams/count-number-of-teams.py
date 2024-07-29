from functools import lru_cache
from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)

        @lru_cache(None)
        def count_increasing_teams(current_index: int, team_size: int) -> int:
            # Base case: found a valid team of size 3
            if team_size == 3:
                return 1
            
            # Base case: reached end of array
            if current_index == n:
                return 0

            valid_teams = 0
            # Recursively count teams with increasing ratings
            for next_index in range(current_index + 1, n):
                if rating[next_index] > rating[current_index]:
                    valid_teams += count_increasing_teams(next_index, team_size + 1)

            return valid_teams

        @lru_cache(None)
        def count_decreasing_teams(current_index: int, team_size: int) -> int:
            # Base case: found a valid team of size 3
            if team_size == 3:
                return 1
            
            # Base case: reached end of array
            if current_index == n:
                return 0

            valid_teams = 0
            # Recursively count teams with decreasing ratings
            for next_index in range(current_index + 1, n):
                if rating[next_index] < rating[current_index]:
                    valid_teams += count_decreasing_teams(next_index, team_size + 1)

            return valid_teams

        teams_count = 0
        # Calculate total teams by considering each soldier as a starting point
        for start_index in range(n):
            teams_count += count_increasing_teams(start_index, 1)
            teams_count += count_decreasing_teams(start_index, 1)

        return teams_count
