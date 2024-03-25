from collections import deque
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = set()
        visited_rooms.add(0)

        queue = deque()
        queue.append(0)

        while queue:
            current_room = queue.popleft()
            for key in rooms[current_room]:
                if key not in visited_rooms:
                    visited_rooms.add(key)
                    queue.append(key)

        return len(visited_rooms) == len(rooms)
