class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        number_of_meetings = [0] * n

        unused = [(i, 0) for i in range(n)]
        used = []

        meetings.sort()

        for i, meeting in enumerate(meetings):
            start, end = meeting
            while not unused or (used and used[0][0] <= start):
                end_time, room = heapq.heappop(used)
                heapq.heappush(unused, (room, end_time))
                    
            room, end_time = heapq.heappop(unused)
            number_of_meetings[room] += 1
            st = max(end_time, start)
            duration = end - start
            heapq.heappush(used, (st + duration, room))

        maxnum = max(number_of_meetings)

        return number_of_meetings.index(maxnum)

        