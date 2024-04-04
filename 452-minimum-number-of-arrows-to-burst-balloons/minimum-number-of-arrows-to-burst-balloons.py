from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort the intervals by their end points
        points.sort(key=lambda x: x[1])

        arrows = 1  # Initialize the number of arrows needed
        first_end = points[0][1]  # Initialize the end point of the first interval

        # Iterate through the sorted intervals
        for x_start, x_end in points:
            # If the start point of the current interval is beyond the end point of the previous interval,
            # it means we need an additional arrow
            if first_end < x_start:
                arrows += 1
                first_end = x_end  # Update the end point for the new arrow

        return arrows
