class Solution:
    def can_place_balls(self, min_gap, positions, m):
        """
        Check if we can place 'm' balls with each ball having at least 'min_gap' gap.
        """
        previous_position = positions[0]
        balls_placed = 1

        for i in range(1, len(positions)):
            current_position = positions[i]
            # If the gap between the current and previous position is at least 'min_gap', place a ball
            if current_position - previous_position >= min_gap:
                balls_placed += 1
                previous_position = current_position
            # If we have placed all 'm' balls, return True
            if balls_placed == m:
                return True
        return False

    def maxDistance(self, positions: List[int], m: int) -> int:
        """
        Find the maximum minimum gap between any two balls that can be placed in the given positions.
        """
        positions.sort()
        left, right = 1, positions[-1] - positions[0]
        max_gap = 0

        while left <= right:
            mid_gap = left + (right - left) // 2
            # Check if we can place all balls with at least 'mid_gap' distance
            if self.can_place_balls(mid_gap, positions, m):
                max_gap = mid_gap
                left = mid_gap + 1
            else:
                right = mid_gap - 1

        return max_gap
