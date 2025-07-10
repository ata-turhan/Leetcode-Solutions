from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        """
        Return the maximum continuous free time in [0, eventTime]
        after moving at most one meeting (keeping its duration).
        """
        n = len(startTime)
        # 1) Build the n+1 free gaps: before, between, and after meetings
        gaps = [startTime[0]]  # gap before the first meeting
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i-1])
        gaps.append(eventTime - endTime[-1])  # gap after the last meeting

        m = n + 1
        # 2) Precompute prefix-maximums and suffix-maximums of the gaps
        pre_max = [0] * m
        pre_max[0] = gaps[0]
        for i in range(1, m):
            pre_max[i] = max(pre_max[i-1], gaps[i])

        suf_max = [0] * m
        suf_max[m-1] = gaps[m-1]
        for i in range(m-2, -1, -1):
            suf_max[i] = max(suf_max[i+1], gaps[i])

        # 3) Track the best without any rescheduling
        best = pre_max[-1]  # same as max(gaps)

        # 4) Try removing (and then re-placing) each meeting
        for i in range(n):
            d = endTime[i] - startTime[i]       # duration of meeting i
            left = gaps[i]                      # free before it
            right = gaps[i+1]                   # free after it
            merged = left + d + right          # free if we remove it

            # largest free interval outside [i, i+1]
            outside_left = pre_max[i-1] if i-1 >= 0 else 0
            outside_right = suf_max[i+2] if i+2 < m else 0
            max_outside = outside_left if outside_left > outside_right else outside_right

            # Option 1: place meeting back into its merged region → free = left + right
            free_lr = left + right
            candidate = max(free_lr, max_outside)

            # Option 2: if there's an outside gap ≥ d, place meeting there:
            #   - merged region becomes fully free (merged)
            #   - outside gap shrinks by d (max_outside - d)
            if max_outside >= d:
                candidate = max(candidate, merged, max_outside - d)

            # update global best
            if candidate > best:
                best = candidate

        return best
