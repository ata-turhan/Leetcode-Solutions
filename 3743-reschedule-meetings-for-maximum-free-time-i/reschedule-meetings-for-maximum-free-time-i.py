from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        """
        Compute the maximum continuous free time achievable within [0, eventTime]
        after rescheduling at most k meetings (keeping durations and order).
        """

        n = len(startTime)
        # Step 1: Build the list of n+1 gaps between meetings
        gaps = [0] * (n + 1)
        # Gap before the first meeting
        gaps[0] = startTime[0]  # time from 0 up to first meeting start
        # Intermediate gaps between meetings i and i+1
        for i in range(n - 1):
            gaps[i + 1] = startTime[i + 1] - endTime[i]
        # Gap after the last meeting
        gaps[n] = eventTime - endTime[-1]

        # Step 2: Use a sliding window of size k+1 to find the max sum of gaps
        window_size = k + 1
        # Initial window sum (first k+1 gaps)
        current_sum = sum(gaps[:window_size])
        max_free = current_sum

        # Slide the window across the rest of the gaps
        for i in range(window_size, n + 1):
            # Subtract gap leaving window, add new gap entering window
            current_sum += gaps[i] - gaps[i - window_size]
            if current_sum > max_free:
                max_free = current_sum

        return max_free
