from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        """
        Count ordered pairs (Alice at upper-left i, Bob at lower-right j) such that the
        axis-aligned rectangle with corners (x_i, y_i) (upper-left) and (x_j, y_j) (lower-right)
        contains no other points on or inside it.

        Approach:
        1) Sort by x ascending, then y descending. For any i < j in this order, x_i <= x_j.
           The y tie-break ensures vertical segments are handled correctly.
        2) Fix i (Alice). Sweep j from i+1 to n-1 (Bob). Maintain:
               m = max{ y_k | i < k < j and y_k <= y_i }   (initialized to -inf)
           Increment answer when y_i >= y_j and m < y_j. This guarantees no k lies in/on
           the rectangle (including fence boundaries).
        3) Update m incrementally using only the immediately previous index (j-1):
               if (j-1) > i and y_{j-1} <= y_i: m = max(m, y_{j-1})

        Complexity: O(n^2) time, O(1) extra space.
        """
        # 1) Sort by x asc, y desc to enforce x_i <= x_j for i < j (and handle vertical lines)
        pts = sorted(points, key=lambda p: (p[0], -p[1]))
        ys = [y for _, y in pts]
        n = len(pts)

        ans = 0
        NEG_INF = -(10**19)

        # 2) For each Alice i, sweep Bob j to the right while tracking max y between i and j
        for i in range(n):
            m = NEG_INF  # max y among (i, j) with y_k <= y_i
            for j in range(i + 1, n):
                k = j - 1  # only one new candidate enters the (i, j) interval at each step
                if k > i and ys[k] <= ys[i]:
                    if ys[k] > m:
                        m = ys[k]

                # Valid iff Alice is above/right of Bob in y, and no interior/on-fence points exist
                if ys[i] >= ys[j] and m < ys[j]:
                    ans += 1

        return ans
