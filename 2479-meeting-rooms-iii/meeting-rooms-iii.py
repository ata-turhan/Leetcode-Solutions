import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Initialize the count of meetings for each room
        number_of_meetings = [0] * n

        # Min-heaps for unused and used rooms
        unused = [(i, 0) for i in range(n)]
        used = []

        # Sort meetings by their start time
        meetings.sort()

        for meeting in meetings:
            start, end = meeting

            # Free up rooms that have finished their meetings
            while not unused or (used and used[0][0] <= start):
                end_time, room = heapq.heappop(used)
                heapq.heappush(unused, (room, end_time))

            # Allocate a room for the current meeting
            room, end_time = heapq.heappop(unused)
            number_of_meetings[room] += 1
            new_start_time = max(end_time, start)
            duration = end - start
            heapq.heappush(used, (new_start_time + duration, room))

        # Find the room with the maximum number of meetings
        max_meetings = max(number_of_meetings)
        return number_of_meetings.index(max_meetings)

# Example usage:
# sol = Solution()
# print(sol.mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]))  # Output: 0
