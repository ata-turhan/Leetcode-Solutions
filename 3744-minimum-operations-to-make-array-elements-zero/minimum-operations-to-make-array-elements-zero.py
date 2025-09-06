from typing import List
import bisect

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        """
        For each query [l, r], the array is [l, l+1, ..., r].
        Let k(x) be the number of times we must apply x := floor(x/4) until x hits 0.
        It's standard that k(x) = floor(log_4 x) + 1 for x >= 1 (and 0 for x == 0, unused here).

        Each operation selects two elements and decreases both of their remaining k by 1.
        If a multiset of tasks requires counts {k_i}, the minimum number of steps when you
        can process two distinct tasks per step is:
            max( max(k_i), ceil( sum(k_i) / 2 ) ).
        (The greedy "pair the two largest" achieves this bound.)

        We therefore need, per [l, r]:
          - K = max_{x in [l,r]} k(x) = floor(log_4 r) + 1
          - S = sum_{x=l..r} k(x)

        Observe that k(x) is constant over blocks [4^t, 4^{t+1}-1], where it equals t+1.
        We precompute powers of 4 and a prefix sum of the total contribution of *full* blocks to
        evaluate S(n) = sum_{x=1..n} k(x) in O(log n) via binary search, then S(l,r) = S(r) - S(l-1).

        Complexity: O(Q log log r_max) ~ O(Q), since there are only ~15 powers of 4 up to 1e9.
        """

        # Precompute powers of 4 up to > 1e9 (constraint upper bound)
        pow4 = [1]
        LIM = 10**9
        while pow4[-1] <= LIM:
            pow4.append(pow4[-1] * 4)
        # pow4: [4^0, 4^1, ..., 4^T] where 4^T > 1e9

        # Precompute contribution of each full block t: all x in [4^t, 4^{t+1}-1] have k = t+1
        # Block size = 4^{t+1} - 4^t = 3 * 4^t, contribution = (t+1) * (3 * 4^t)
        contrib_full = []
        for t in range(len(pow4) - 1):
            block_size = pow4[t+1] - pow4[t]
            contrib_full.append((t + 1) * block_size)

        # Prefix sum of full-block contributions: pref_full[t] = sum_{i=0..t-1} contrib_full[i]
        pref_full = [0]
        for c in contrib_full:
            pref_full.append(pref_full[-1] + c)

        def sum_k_upto(n: int) -> int:
            """Return S(n) = sum_{x=1..n} k(x). Assumes n >= 0."""
            if n <= 0:
                return 0
            # Find T s.t. 4^T <= n < 4^{T+1}
            T = bisect.bisect_right(pow4, n) - 1
            # Sum of all full blocks below T
            full = pref_full[T]
            # Partial block at level T contributes (T+1) for each x in [4^T .. n]
            partial_cnt = n - pow4[T] + 1
            return full + (T + 1) * partial_cnt

        def max_k(r: int) -> int:
            """Return K = max k(x) for x in [1..r] (and thus also for [l..r])."""
            # floor_log4(r) = largest T with 4^T <= r; K = T+1
            T = bisect.bisect_right(pow4, r) - 1
            return T + 1

        total = 0
        for l, r in queries:
            S = sum_k_upto(r) - sum_k_upto(l - 1)
            K = max_k(r)  # since k is nondecreasing with x, max over [l,r] is at r
            # Minimal operations for this query
            ans = max(K, (S + 1) // 2)  # ceil(S/2) = (S+1)//2
            total += ans

        return total
