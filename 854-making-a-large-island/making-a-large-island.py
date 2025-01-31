class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0
        
        # Step 1: Identify each connected component of 1s and assign a unique index/id
        # Also calculate the area of each component.
        component_id = 2  # Start labeling from 2 to differentiate from original 0s and 1s
        area = {}         # Key: component_id, Value: area of that component

        def dfs(r, c, index):
            """Perform DFS to label the connected component and count its size."""
            stack = [(r, c)]
            grid[r][c] = index
            component_size = 1

            while stack:
                x, y = stack.pop()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = index
                        stack.append((nx, ny))
                        component_size += 1
            return component_size

        # Label each island and store its area
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[component_id] = dfs(i, j, component_id)
                    component_id += 1
        
        # If there's no island at all, flipping one cell from 0 to 1 results in area = 1
        if not area:
            return 1
        
        # Step 2: For each 0, check the unique neighboring components and calculate the sum of their areas
        # plus 1 (for flipping the 0 into a 1).
        max_area = max(area.values())  # The area of the largest existing island
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    # Find unique component ids around this cell
                    unique_components = set()
                    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] != 0:
                            unique_components.add(grid[x][y])
                    
                    # Sum the areas of all unique neighboring components + 1 for this flip
                    new_area = 1
                    for comp_id in unique_components:
                        new_area += area[comp_id]
                    
                    max_area = max(max_area, new_area)
        
        return max_area
