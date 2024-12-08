from heapq import heappop, heappush
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        """
        Finds the maximum sum of values from at most two non-overlapping events.

        :param events: List of events, where each event is represented as [start, end, value].
        :return: The maximum sum of values from two non-overlapping events.
        """
        # Step 1: Sort events by start time to process them in order.
        events.sort()

        ended_events = []  # Min-heap to track ended events by their end time
        max_ended_val = 0  # The maximum value among events that have already ended
        max_sum = 0  # Result variable to track the maximum sum of values

        for current_start, current_end, current_value in events:
            # Step 2: Remove events from the heap that ended before the current event's start time
            while ended_events and ended_events[0][0] < current_start:
                max_ended_val = max(max_ended_val, ended_events[0][1])  # Update max value of ended events
                heappop(ended_events)

            # Step 3: Update the maximum sum using the current event and the best ended event
            max_sum = max(max_sum, current_value + max_ended_val)

            # Step 4: Add the current event to the heap
            heappush(ended_events, [current_end, current_value])

        return max_sum
