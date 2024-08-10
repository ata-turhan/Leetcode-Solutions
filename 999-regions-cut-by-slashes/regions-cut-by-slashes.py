class UnionFind:
    def __init__(self, n):
        # Initialize the parent list for each element as itself, rank list to track tree depth,
        # and the count of disjoint sets (initially equal to the number of elements).
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, p):
        # Find the root of the element p with path compression.
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        # Union by rank: attach the tree with lesser rank to the one with greater rank.
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1
            self.count -= 1  # Decrease the count of disjoint sets.

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UnionFind(4 * n * n)  # Each cell is split into 4 regions.

        def index(i, j, k):
            # Map the cell (i, j) and region k to a unique index.
            return (i * n + j) * 4 + k

        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    # Union regions corresponding to '/'
                    uf.union(index(i, j, 0), index(i, j, 3))
                    uf.union(index(i, j, 1), index(i, j, 2))
                elif grid[i][j] == '\\':
                    # Union regions corresponding to '\'
                    uf.union(index(i, j, 0), index(i, j, 1))
                    uf.union(index(i, j, 2), index(i, j, 3))
                else:
                    # Union all 4 regions if the cell is empty
                    uf.union(index(i, j, 0), index(i, j, 1))
                    uf.union(index(i, j, 1), index(i, j, 2))
                    uf.union(index(i, j, 2), index(i, j, 3))

                # Connect the current cell's regions with the neighboring cells' regions.
                if i > 0:
                    uf.union(index(i, j, 0), index(i-1, j, 2))
                if j > 0:
                    uf.union(index(i, j, 3), index(i, j-1, 1))

        return uf.count  # Return the number of disjoint sets, which corresponds to the number of regions.
