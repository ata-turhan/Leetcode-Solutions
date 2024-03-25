class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set()
        visited = set()
        q = deque()
        q.append(0)
        visited.add(0)

        while q:
            room = q.popleft()
            for key in rooms[room]:
                keys.add(key)
                if key not in visited:
                    visited.add(key)
                    q.append(key)

        return len(visited) == len(rooms)
        