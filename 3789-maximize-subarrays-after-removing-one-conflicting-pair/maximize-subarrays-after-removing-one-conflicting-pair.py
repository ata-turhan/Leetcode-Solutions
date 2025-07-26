from typing import List
import heapq

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        """
        Return the maximum number of subarrays of [1..n] that avoid having both
        elements of any conflicting pair, after removing exactly one pair.
        """
        # 1) Group pairs by their left endpoint.
        events_by_left = [[] for _ in range(n + 1)]
        num_pairs = len(conflictingPairs)
        for pid, (a, b) in enumerate(conflictingPairs):
            if a > b:
                a, b = b, a
            # We store (b-1, pair_id) since any subarray ending at >= b is invalid if it includes a.
            events_by_left[a].append((b - 1, pid))
        
        # 2) Sweep i from n down to 1, maintaining a min‑heap of all active (end_limit, pair_id).
        min_heap = []
        total_f_sum = 0          # Sum of f[i] over all start indices i
        gain = [0] * num_pairs   # gain[pid] = how much f[i] rises if we remove pair pid
        
        for i in range(n, 0, -1):
            # Activate all pairs with left endpoint == i
            for end_limit, pid in events_by_left[i]:
                heapq.heappush(min_heap, (end_limit, pid))
            
            if min_heap:
                # The tightest constraint for f[i]
                f_i, top_pid = min_heap[0]
                # Determine the second-tightest constraint:
                if len(min_heap) >= 3:
                    # In a binary heap, the second smallest is one of the root's two children.
                    sec_i = min(min_heap[1][0], min_heap[2][0])
                elif len(min_heap) == 2:
                    sec_i = min_heap[1][0]
                else:
                    sec_i = n
            else:
                # No constraints remain → subarray can extend to n
                f_i = sec_i = n
                top_pid = -1  # indicates "no real pair" controls
            
            # Accumulate the base sum of f[i]
            total_f_sum += f_i
            # If a real pair controls f[i], record its contribution to gain
            if top_pid != -1:
                gain[top_pid] += (sec_i - f_i)
        
        # 3) Compute the answer with all pairs:
        #    Sum_{i=1..n}(f[i] - i + 1) = total_f_sum - (n(n+1)/2) + n
        total_subarrays = n * (n + 1) // 2
        base_answer = total_f_sum - total_subarrays + n
        
        # 4) Best removal adds the maximum gain
        max_gain = max(gain) if gain else 0
        return base_answer + max_gain
