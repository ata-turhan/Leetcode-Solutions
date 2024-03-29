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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # Initialize UnionFind data structure
        n = len(s)
        uf = UnionFind(n)
        
        # Union all pairs of indices
        for a, b in pairs:
            uf.union(a, b)
        
        # Build character mapping for each disjoint set
        char_mapping = defaultdict(list)
        for i in range(n):
            char_mapping[uf.find(i)].append(s[i])
        
        # Sort characters in each disjoint set
        for char_set in char_mapping.values():
            char_set.sort(reverse=True)
        
        # Reconstruct the string using character mapping
        result = []
        for i in range(n):
            result.append(char_mapping[uf.find(i)].pop())
        
        return ''.join(result)
