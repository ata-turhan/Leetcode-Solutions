from typing import List

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        """
        Return the number of ways to paint an m x n grid with 3 colors
        such that no two adjacent cells (horizontally or vertically)
        share the same color. Result modulo 1_000_000_007.
        """
        MOD: int = 10**9 + 7

        # Helper: check if a single column mask is valid (no two vertical neighbors equal)
        def is_valid_column(mask: int) -> bool:
            prev_color = mask % 3
            mask //= 3
            for _ in range(1, m):
                curr_color = mask % 3
                if curr_color == prev_color:
                    return False
                prev_color = curr_color
                mask //= 3
            return True

        # Helper: check if two column masks are compatible (no two horizontal neighbors equal)
        def are_compatible(mask1: int, mask2: int) -> bool:
            for _ in range(m):
                if (mask1 % 3) == (mask2 % 3):
                    return False
                mask1 //= 3
                mask2 //= 3
            return True

        # 1. Generate all valid column masks
        total_states = 3**m
        valid_masks: List[int] = [
            mask for mask in range(total_states)
            if is_valid_column(mask)
        ]
        k = len(valid_masks)

        # 2. Precompute compatibility: comp[j] = list of i such that valid_masks[i] ➔ valid_masks[j] is allowed
        comp: List[List[int]] = [[] for _ in range(k)]
        for j in range(k):
            mj = valid_masks[j]
            for i in range(k):
                if are_compatible(valid_masks[i], mj):
                    comp[j].append(i)

        # 3. Initialize DP for the first column: each valid pattern counts as 1
        dp: List[int] = [1] * k

        # 4. Propagate DP across the remaining n-1 columns
        for _ in range(1, n):
            new_dp: List[int] = [0] * k
            for j in range(k):
                total = 0
                for i in comp[j]:
                    total += dp[i]
                new_dp[j] = total % MOD
            dp = new_dp

        # 5. Sum all possibilities for the last column
        return sum(dp) % MOD
