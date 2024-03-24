class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        visited = set()
        q = deque()

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j, 0))
        
        moves = [
            [-1, 0],
            [0, 1],
            [1, 0],
            [0, -1]
        ]

        while q:
            i, j, dist = q.popleft()
            for move in moves:
                ri, rj = i + move[0], j + move[1]
                if ri in range(len(rooms)) and rj in range(len(rooms[0])) \
                and (ri, rj) not in visited and rooms[ri][rj] == 2**31-1:
                    visited.add((ri, rj))
                    rooms[ri][rj] = dist + 1
                    q.append((ri, rj, dist+1))


        
        