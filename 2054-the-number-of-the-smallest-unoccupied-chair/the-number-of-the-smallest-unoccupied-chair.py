import heapq
from typing import List

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        # List of available seat numbers (0 to n-1)
        available_seats = list(range(n))
        # Min-heap to store (leave_time, seat_number) for seated friends
        seated_friends = []
        
        # Add indices to times for easier identification and sort by arrival times
        times_with_idx = [(arrival, leave, i) for i, (arrival, leave) in enumerate(times)]
        times_with_idx.sort()

        # Iterate through each friend's arrival and leaving times
        for i in range(n):
            arrival, leave, friend_idx = times_with_idx[i]

            # Free up seats for friends whose leave times have passed
            while seated_friends and seated_friends[0][0] <= arrival:
                _, seat_to_free = heapq.heappop(seated_friends)
                heapq.heappush(available_seats, seat_to_free)

            # Assign the smallest available seat to the current friend
            available_seat = heapq.heappop(available_seats)
            heapq.heappush(seated_friends, (leave, available_seat))

            # If the current friend is the target friend, return the seat they took
            if friend_idx == targetFriend:
                return available_seat
