class UnionFind:
    def __init__(self, size):
        # Initialize parent pointers and rank for union-find
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, u):
        # Path compression for finding the root of u
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # Union by rank for merging sets containing u and v
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Initialize union-find structures for Alice and Bob
        uf_alice = UnionFind(n + 1)
        uf_bob = UnionFind(n + 1)
        
        # Sort edges in descending order to prioritize type 3 edges
        edges.sort(reverse=True)
        
        edges_used = 0
        
        # Process edges
        for type_, u, v in edges:
            if type_ == 3:
                # Use type 3 edges for both Alice and Bob
                if uf_alice.union(u, v) | uf_bob.union(u, v):
                    edges_used += 1
            elif type_ == 1:
                # Use type 1 edges for Alice
                if uf_alice.union(u, v):
                    edges_used += 1
            elif type_ == 2:
                # Use type 2 edges for Bob
                if uf_bob.union(u, v):
                    edges_used += 1
        
        # Check if both Alice and Bob can traverse the entire graph
        if all(uf_alice.find(i) == uf_alice.find(1) for i in range(2, n + 1)) and \
           all(uf_bob.find(i) == uf_bob.find(1) for i in range(2, n + 1)):
            return len(edges) - edges_used
        return -1
