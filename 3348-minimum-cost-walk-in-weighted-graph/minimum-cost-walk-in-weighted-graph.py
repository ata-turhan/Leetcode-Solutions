class UnionFind():
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.weight = [2**31-1] * n
    
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y, weight):
        x_root, y_root = self.find(x), self.find(y)
        if self.rank[x_root] > self.rank[y_root]:
            self.root[y_root] = x_root
        elif self.rank[x_root] < self.rank[y_root]:
            self.root[x_root] = y_root
        else:
            self.root[y_root] = x_root
            self.rank[x_root] += 1
        self.weight[x_root] = self.weight[y_root] = self.weight[x_root] & self.weight[y_root] & weight

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UnionFind(n)
        for u, v, w in edges:
            uf.union(u, v, w)
        res = []
        for q in query:
            if q[0] == q[1]:
                res.append(0)
                print("ata")
            elif uf.find(q[0]) != uf.find(q[1]):
                res.append(-1)
            else:
                res.append(uf.weight[uf.find(q[0])])
        return res


            