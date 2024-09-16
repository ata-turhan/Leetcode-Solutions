from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert time points to minutes since midnight
        time_in_minutes: List[int] = []
        for time_point in timePoints:
            total_minutes: int = int(time_point[:2]) * 60 + int(time_point[3:])
            time_in_minutes.append(total_minutes)

        # Sort the time points in minutes
        time_in_minutes.sort()

        # Initialize the minimum difference as infinity
        min_difference: int = float("inf")

        # Find the minimum difference between consecutive time points
        for i in range(1, len(time_in_minutes)):
            min_difference = min(min_difference, time_in_minutes[i] - time_in_minutes[i - 1])

        # Account for the circular nature of time (difference between the last and first point)
        min_difference = min(min_difference, 24 * 60 - (time_in_minutes[-1] - time_in_minutes[0]))

        return min_difference
