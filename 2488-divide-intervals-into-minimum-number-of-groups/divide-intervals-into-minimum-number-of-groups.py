from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Create events for starting and ending points of intervals
        start_events = [(start, 1) for start, _ in intervals]
        end_events = [(end + 1, -1) for _, end in intervals]  # end + 1 to mark the end of an interval
        
        # Combine and sort all the events
        events = start_events + end_events
        events.sort()

        max_groups = 0
        active_groups = 0
        
        # Traverse through each event, adjusting active group count
        for _, value in events:
            active_groups += value
            max_groups = max(max_groups, active_groups)
        
        return max_groups
