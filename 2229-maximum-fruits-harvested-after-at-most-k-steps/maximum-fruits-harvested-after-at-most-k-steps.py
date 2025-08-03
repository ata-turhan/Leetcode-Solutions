from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        """
        Return the maximum fruits that can be harvested starting from startPos
        with at most k steps on an infinite x-axis.
        """
        n = len(fruits)
        # Extract positions and amounts
        positions = [p for p, a in fruits]
        amounts   = [a for p, a in fruits]
        
        # Build prefix sums: ps[i] = total fruits in amounts[0..i-1]
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i+1] = ps[i] + amounts[i]
        
        def range_sum(L: int, R: int) -> int:
            """Sum of fruits amounts[L..R] inclusive."""
            return ps[R+1] - ps[L]
        
        result = 0
        
        # 1) Only move right: [startPos, startPos + k]
        right_end = startPos + k
        left_idx  = bisect_left(positions, startPos)
        right_idx = bisect_right(positions, right_end) - 1
        if left_idx <= right_idx:
            result = max(result, range_sum(left_idx, right_idx))
        
        # 2) Only move left: [startPos - k, startPos]
        left_start = startPos - k
        left_idx2  = bisect_left(positions, left_start)
        right_idx2 = bisect_right(positions, startPos) - 1
        if left_idx2 <= right_idx2:
            result = max(result, range_sum(left_idx2, right_idx2))
        
        # 3) Go left first, then turn and go right
        #    Iterate over furthest-left fruit index i we choose to visit
        i = bisect_right(positions, startPos) - 1
        while i >= 0:
            dist_left = startPos - positions[i]
            if dist_left > k:
                break  # can't even reach this fruit
            # Steps remaining for rightward travel after returning to start
            rem = k - 2 * dist_left
            if rem >= 0:
                # furthest right we can reach
                right_bound_idx = bisect_right(positions, startPos + rem) - 1
                total = range_sum(i, right_bound_idx)
                result = max(result, total)
            i -= 1
        
        # 4) Go right first, then turn and go left
        j = bisect_left(positions, startPos)
        while j < n:
            dist_right = positions[j] - startPos
            if dist_right > k:
                break  # can't even reach this fruit
            rem = k - 2 * dist_right
            if rem >= 0:
                # furthest left we can then reach
                left_bound_idx = bisect_left(positions, startPos - rem)
                total = range_sum(left_bound_idx, j)
                result = max(result, total)
            j += 1
        
        return result
