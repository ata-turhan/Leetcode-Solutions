from typing import List, Dict

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Sort an n x n matrix by its TL->BR diagonals:
          - Diagonals with key k = i - j >= 0 (on/below main)  -> non-increasing.
          - Diagonals with key k = i - j < 0  (above main)      -> non-decreasing.
        """
        n = len(grid)

        # 1) Bucket values by diagonal key k = i - j
        diags: Dict[int, List[int]] = {}
        for i in range(n):
            for j in range(n):
                k = i - j
                diags.setdefault(k, []).append(grid[i][j])

        # 2) Sort each diagonal according to the region rule
        for k, vals in diags.items():
            if k >= 0:
                vals.sort(reverse=True)   # non-increasing for bottom-left incl. main
            else:
                vals.sort()               # non-decreasing for top-right

        # 3) Write back using pointers per diagonal (avoid pop(0))
        idx: Dict[int, int] = {k: 0 for k in diags}
        for i in range(n):
            for j in range(n):
                k = i - j
                grid[i][j] = diags[k][idx[k]]
                idx[k] += 1

        return grid
