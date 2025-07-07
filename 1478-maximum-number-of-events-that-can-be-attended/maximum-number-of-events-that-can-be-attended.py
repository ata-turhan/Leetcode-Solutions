import heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        Return the maximum number of events that can be attended.
        Greedy strategy: each day, attend the available event with the earliest end.
        """
        # 1. Sort events by start day
        events.sort(key=lambda ev: ev[0])

        min_heap = []     # will store end days of available events
        count = 0         # total events attended
        day = 0           # current day pointer
        i, n = 0, len(events)

        # 2. Process until no more events and heap is empty
        while i < n or min_heap:
            # If no events are pending, jump day to next event's start
            if not min_heap:
                day = events[i][0]

            # 3. Add all events that have started by 'day'
            while i < n and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            # 4. Remove any events that already ended before 'day'
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # 5. Attend the event that ends soonest (if any)
            if min_heap:
                heapq.heappop(min_heap)
                count += 1
                day += 1

        return count
