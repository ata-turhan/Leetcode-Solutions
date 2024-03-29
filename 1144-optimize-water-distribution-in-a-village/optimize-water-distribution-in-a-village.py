class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            elif self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            else:
                self.parent[y_root] = x_root
                self.rank[x_root] += 1

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # Create a virtual node connected to all houses with edges weighted by the costs to build wells
        virtual_node_edges = [(0, i + 1, cost) for i, cost in enumerate(wells)]
        all_edges = virtual_node_edges + pipes
        
        # Sort all edges by their costs
        all_edges.sort(key=lambda x: x[2])
        
        # Initialize UnionFind data structure
        uf = UnionFind(n + 1)
        
        # Perform Kruskal's algorithm to find the MST
        total_cost = 0
        for edge in all_edges:
            house1, house2, cost = edge
            if uf.find(house1) != uf.find(house2):
                uf.union(house1, house2)
                total_cost += cost
        
        return total_cost
