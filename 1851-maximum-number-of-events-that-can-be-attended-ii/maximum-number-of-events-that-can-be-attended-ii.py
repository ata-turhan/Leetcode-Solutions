from typing import List
import bisect

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """
        Return the maximum sum of values by attending at most k non-overlapping events.

        Approach:
        1. Sort events by start day.
        2. Precompute for each event the index of the next non-overlapping event.
        3. Use DP where dp[i][j] = best value from events[i:] with j attends remaining.
        4. Fill dp bottom-up and return dp[0][k].
        Time Complexity: O(n log n + n * k)
        Space Complexity: O(n * k)
        """
        # Number of events
        n_events = len(events)
        
        # 1. Sort by start day
        events.sort(key=lambda event: event[0])
        
        # Extract start days for binary search
        start_days = [event[0] for event in events]
        
        # 2. Compute next_index array via binary search
        #    next_index[i] = smallest index j > i with start_days[j] > events[i].end
        next_index = [0] * n_events
        for i, (start_i, end_i, _) in enumerate(events):
            # bisect_right finds first start > end_i
            next_index[i] = bisect.bisect_right(start_days, end_i)
        
        # 3. Initialize DP table of size (n_events+1) x (k+1)
        #    dp_table[i][j] = max value from i..end if you can attend up to j events
        dp_table = [[0] * (k + 1) for _ in range(n_events + 1)]
        
        # 4. Fill DP bottom-up
        #    Iterate i from last event back to first
        for i in range(n_events - 1, -1, -1):
            start_i, end_i, value_i = events[i]
            for attends_left in range(1, k + 1):
                # Option 1: skip this event
                skip_value = dp_table[i + 1][attends_left]
                # Option 2: take this event, then jump to next_index[i] with one fewer attend
                take_value = value_i + dp_table[next_index[i]][attends_left - 1]
                # Choose the better of skip vs. take
                dp_table[i][attends_left] = max(skip_value, take_value)
        
        # 5. Answer is dp_table[0][k]
        return dp_table[0][k]
