from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        """
        Min-sum cover of all 1s by 3 non-overlapping axis-aligned rectangles.
        Key idea (per hints):
          - Any optimal arrangement allows isolating at least one rectangle by a global
            horizontal or vertical cut that doesn't intersect the other rectangles.
          - After isolating one part by a straight cut, the remainder can be split
            again (either by two cuts in the same direction or by an orthogonal cut).
        With R, C <= 30, we can afford O(R^2*C^2) style enumeration with tight
        area computations on submatrices.

        We consider four families:
          1) Two horizontal cuts (3 horizontal bands).
          2) Two vertical cuts (3 vertical bands).
          3) One horizontal band + best vertical 2-split on the rest (both choices: top single or bottom single).
          4) One vertical band + best horizontal 2-split on the rest (both choices: left single or right single).

        A "rectangle area" for a submatrix is the tight bounding box of all 1s within
        that submatrix; if no 1s exist, its area is 0 (valid since we need 3 rectangles
        overall but a band may contribute 0 if it contains no 1s).
        """

        R, C = len(grid), len(grid[0])

        # Compute tight bounding-box area for 1s inside submatrix [r1..r2] x [c1..c2].
        def area(r1: int, r2: int, c1: int, c2: int) -> int:
            minr, maxr, minc, maxc = R, -1, C, -1
            for r in range(r1, r2 + 1):
                row = grid[r]
                for c in range(c1, c2 + 1):
                    if row[c] == 1:
                        if r < minr: minr = r
                        if r > maxr: maxr = r
                        if c < minc: minc = c
                        if c > maxc: maxc = c
            if maxr == -1:  # no 1s
                return 0
            return (maxr - minr + 1) * (maxc - minc + 1)

        # Best sum of TWO rectangles when splitting the submatrix horizontally by a single row cut.
        # We minimize over k splitting into [r1..k] and [k+1..r2].
        def best_two_split_rows(r1: int, r2: int, c1: int, c2: int) -> int:
            if r1 > r2:
                return 0
            best = float('inf')
            for k in range(r1, r2):
                a = area(r1, k, c1, c2)
                b = area(k + 1, r2, c1, c2)
                s = a + b
                if s < best:
                    best = s
            # If r1==r2 (no valid split), treat as one band; but caller only uses when r2>=r1+1
            return 0 if best == float('inf') else best

        # Best sum of TWO rectangles when splitting the submatrix vertically by a single column cut.
        # We minimize over k splitting into [c1..k] and [k+1..c2].
        def best_two_split_cols(r1: int, r2: int, c1: int, c2: int) -> int:
            if c1 > c2:
                return 0
            best = float('inf')
            for k in range(c1, c2):
                a = area(r1, r2, c1, k)
                b = area(r1, r2, k + 1, c2)
                s = a + b
                if s < best:
                    best = s
            return 0 if best == float('inf') else best

        ans = float('inf')

        # Case 1: Two horizontal cuts (three horizontal bands)
        # Bands: [0..i], [i+1..j], [j+1..R-1]
        for i in range(R - 2):
            for j in range(i + 1, R - 1):
                s = (
                    area(0, i, 0, C - 1) +
                    area(i + 1, j, 0, C - 1) +
                    area(j + 1, R - 1, 0, C - 1)
                )
                if s < ans:
                    ans = s

        # Case 2: Two vertical cuts (three vertical bands)
        # Bands: [0..k], [k+1..l], [l+1..C-1]
        for k in range(C - 2):
            for l in range(k + 1, C - 1):
                s = (
                    area(0, R - 1, 0, k) +
                    area(0, R - 1, k + 1, l) +
                    area(0, R - 1, l + 1, C - 1)
                )
                if s < ans:
                    ans = s

        # Case 3: One horizontal band + vertical 2-split on the remainder.
        # Option A: top band single, bottom band 2-vertical-split
        for i in range(R - 1):
            top = area(0, i, 0, C - 1)
            bottom_best = best_two_split_cols(i + 1, R - 1, 0, C - 1)
            s = top + bottom_best
            if s < ans:
                ans = s

            # Option B: bottom band single, top band 2-vertical-split
            bottom = area(i + 1, R - 1, 0, C - 1)
            top_best = best_two_split_cols(0, i, 0, C - 1)
            s = bottom + top_best
            if s < ans:
                ans = s

        # Case 4: One vertical band + horizontal 2-split on the remainder.
        # Option A: left band single, right band 2-horizontal-split
        for j in range(C - 1):
            left = area(0, R - 1, 0, j)
            right_best = best_two_split_rows(0, R - 1, j + 1, C - 1)
            s = left + right_best
            if s < ans:
                ans = s

            # Option B: right band single, left band 2-horizontal-split
            right = area(0, R - 1, j + 1, C - 1)
            left_best = best_two_split_rows(0, R - 1, 0, j)
            s = right + left_best
            if s < ans:
                ans = s

        return ans
