class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_servers = [set() for _ in range(rows)]
        col_servers = [set() for _ in range(cols)]

        communicated_servers = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_servers[i].add((i, j))
                    col_servers[j].add((i, j))

        for i in range(rows):
            if len(row_servers[i]) > 1:
                communicated_servers |= row_servers[i]


        for j in range(cols):
            if len(col_servers[j]) > 1:
                communicated_servers |= col_servers[j]

        
        return len(communicated_servers)
        