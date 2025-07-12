from functools import lru_cache
from typing import List, Tuple

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        """
        Compute the earliest and latest rounds in which `firstPlayer` and `secondPlayer`
        can face each other in an n‑player tournament where in each round:
          - Players are paired front-to-back.
          - Winners advance and are re-sorted by original player number.
          - The middle player (if odd) auto-advances.
        We use a DP on states (m, l, r), enumerating how other matches can
        distribute survivors into regions A (<l), B (between l and r), C (>r).
        """

        @lru_cache(None)
        def dp(m: int, l: int, r: int) -> Tuple[int, int]:
            # If they are paired this round
            if l + r == m + 1:
                return (1, 1)

            half = m // 2

            # Identify which pair indices contain our two players
            pair_l = l if l <= m + 1 - l else m + 1 - l
            pair_r = r if r <= m + 1 - r else m + 1 - r

            # Build category list for all OTHER matches (excluding special pairs)
            cats = []
            for p in range(1, half + 1):
                if p == pair_l or p == pair_r:
                    continue
                low, high = p, m + 1 - p
                # Region by comparison to l and r
                def region(idx):
                    if idx < l:   return 'A'
                    if idx > r:   return 'C'
                    return 'B'
                cats.append(''.join(sorted((region(low), region(high)))))

            # Mid‑round bye classification
            has_mid = (m % 2 == 1)
            if has_mid:
                mid = half + 1
                if mid == l or mid == r:
                    mid_cat = None
                elif mid < l:
                    mid_cat = 'A'
                elif mid > r:
                    mid_cat = 'C'
                else:
                    mid_cat = 'B'

            # DP over OTHER matches: dp_states tracks (a, b, c) survivors counts
            dp_states = {(0, 0, 0)}
            for cat in cats:
                next_states = set()
                for a, b, c in dp_states:
                    if   cat == 'AA': next_states.add((a + 1, b,     c))
                    elif cat == 'BB': next_states.add((a,     b + 1, c))
                    elif cat == 'CC': next_states.add((a,     b,     c + 1))
                    elif cat == 'AB':
                        next_states.add((a + 1, b,     c))
                        next_states.add((a,     b + 1, c))
                    elif cat == 'BC':
                        next_states.add((a,     b + 1, c))
                        next_states.add((a,     b,     c + 1))
                    elif cat == 'AC':
                        next_states.add((a + 1, b,     c))
                        next_states.add((a,     b,     c + 1))
                dp_states = next_states

            # Incorporate the middle bye (if it’s neither first nor second)
            final_states = set()
            if has_mid and mid_cat is not None:
                for a, b, c in dp_states:
                    if   mid_cat == 'A': final_states.add((a + 1, b,     c))
                    elif mid_cat == 'B': final_states.add((a,     b + 1, c))
                    else:                final_states.add((a,     b,     c + 1))
            else:
                final_states = dp_states

            # Recurse on each resulting next‑round state
            earliest, latest = float('inf'), 0
            m2 = (m + 1) // 2
            for a2, b2, c2 in final_states:
                new_l = a2 + 1
                new_r = a2 + b2 + 2
                e_sub, l_sub = dp(m2, new_l, new_r)
                earliest = min(earliest, e_sub + 1)
                latest   = max(latest,   l_sub + 1)

            return (earliest, latest)

        e, l = dp(n, firstPlayer, secondPlayer)
        return [e, l]
