class UnionFind:
    def __init__(self, size):
        # Initialize parent array with each element as its own root
        self.parent = [i for i in range(size)]
        # Initialize rank array to track the height of each tree
        self.rank = [1] * size
        # Initialize component count to the size initially
        self.component_count = size

    def find(self, x):
        # Find the root of the set containing element x
        if x != self.parent[x]:
            # Path compression: set parent of x to the root of its set
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union two elements x and y
        x_root, y_root = self.find(x), self.find(y)

        if x_root != y_root:
            # Union by rank: attach the smaller tree to the root of the larger tree
            if self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
                self.rank[x_root] += self.rank[y_root]
            else:
                self.parent[x_root] = y_root
                self.rank[y_root] += self.rank[x_root]
            # Decrease component count as two components are merged
            self.component_count -= 1

    def get_component_count(self):
        # Get the current number of connected components
        return self.component_count


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initialize UnionFind data structure
        union_find = UnionFind(n)
        
        # Iterate through each edge
        for node1, node2 in edges:
            union_find.union(node1, node2)   

        return union_find.get_component_count()
        