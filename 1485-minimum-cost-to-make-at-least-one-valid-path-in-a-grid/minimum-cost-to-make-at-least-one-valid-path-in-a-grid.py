class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        m, n = len(grid), len(grid[0])
        
        # Directions mapped to the sign on the grid:
        # 1 -> right, 2 -> left, 3 -> down, 4 -> up
        # We store them as (dx, dy)
        directions = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0)
        }
        
        # Distance array to hold the minimum cost to get to each cell
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        # Deque for 0-1 BFS
        dq = deque()
        dq.append((0, 0))
        
        while dq:
            x, y = dq.popleft()
            cost_so_far = dist[x][y]
            
            # If we've reached the bottom-right cell, we can return immediately
            if x == m - 1 and y == n - 1:
                return cost_so_far
            
            # Explore all 4 directions
            for idx, (dx, dy) in enumerate([(0,1), (0,-1), (1,0), (-1,0)], start=1):
                nx, ny = x + dx, y + dy
                # Check boundaries
                if 0 <= nx < m and 0 <= ny < n:
                    # Cost is 0 if the sign's indicated direction is exactly (dx, dy)
                    # sign for (x, y) = grid[x][y] which is 1-based (1=right,2=left,3=down,4=up)
                    # idx is also 1-based in our enumeration: 1->(0,1),2->(0,-1),3->(1,0),4->(-1,0)
                    if idx == grid[x][y]:
                        new_cost = cost_so_far
                    else:
                        new_cost = cost_so_far + 1
                    
                    # If we find a cheaper cost, update and push into deque
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        # If cost is the same, push left; if increased by 1, push right
                        if new_cost == cost_so_far:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))
        
        # If we exhaust the deque without returning, the dist array at bottom-right is the answer
        return dist[m-1][n-1]
