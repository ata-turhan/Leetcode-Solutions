class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        ended_events = []
        max_ended_val = 0
        max_sum = 0

        for event in events:
            cur_start, cur_end, cur_val = event
            while ended_events and ended_events[0][0] < cur_start:
                max_ended_val = max(max_ended_val, ended_events[0][1])
                heappop(ended_events)
            max_sum = max(max_sum, cur_val + max_ended_val)

            heappush(ended_events, [cur_end, cur_val])

        return max_sum
        