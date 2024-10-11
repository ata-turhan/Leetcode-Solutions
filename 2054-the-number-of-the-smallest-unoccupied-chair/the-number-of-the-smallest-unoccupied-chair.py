import heapq
from typing import List

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        num_friends = len(times)
        # List of available chair numbers (0 to num_friends - 1)
        available_chairs = list(range(num_friends))
        # Min-heap to store (leave_time, chair_number) for currently seated friends
        occupied_chairs = []
        
        # Include the friend index in times, then sort by arrival times
        times_with_index = [(arrival, leave, index) for index, (arrival, leave) in enumerate(times)]
        times_with_index.sort()

        # Iterate through each friend's arrival and leave times
        for arrival_time, leave_time, friend_index in times_with_index:
            
            # Free up chairs for friends whose leave times have passed
            while occupied_chairs and occupied_chairs[0][0] <= arrival_time:
                _, chair_to_free = heapq.heappop(occupied_chairs)
                heapq.heappush(available_chairs, chair_to_free)

            # Assign the smallest available chair to the current friend
            smallest_available_chair = heapq.heappop(available_chairs)
            heapq.heappush(occupied_chairs, (leave_time, smallest_available_chair))

            # If the current friend is the target friend, return the chair number assigned
            if friend_index == targetFriend:
                return smallest_available_chair
