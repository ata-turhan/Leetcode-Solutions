class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        # Perform path compression to make future queries faster
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find the roots of the elements
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by rank to keep the tree shallow
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def add(self, x):
        # Add a new element with itself as its own parent
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()

        for x, y in stones:
            uf.add(x)     # Add the row component
            uf.add(~y)    # Add the column component with a negated value to differentiate
            uf.union(x, ~y)  # Union the row and column to form a component

        # Calculate the number of unique components
        unique_components = len(set(uf.find(x) for x, y in stones))
        
        # The result is the total stones minus the number of unique components
        return len(stones) - unique_components
