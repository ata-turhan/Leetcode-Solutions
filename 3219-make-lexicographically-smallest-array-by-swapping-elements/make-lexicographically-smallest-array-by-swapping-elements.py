from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Step 1: Sort the array by value along with original indices
        paired = [(val, idx) for idx, val in enumerate(nums)]
        paired.sort(key=lambda x: x[0])

        n = len(nums)
        dsu = DSU(n)

        # Step 2: Union indices whose values are consecutive and differ by <= limit
        for i in range(1, n):
            if paired[i][0] - paired[i-1][0] <= limit:
                # Union the original indices of these two adjacent values
                dsu.union(paired[i][1], paired[i-1][1])

        # Step 3: Group indices by their DSU root to form connected components
        from collections import defaultdict
        components = defaultdict(list)
        for i in range(n):
            root = dsu.find(i)
            components[root].append(i)

        # Step 4: For each connected component, sort the indices and the corresponding values
        #         then place the sorted values back by index.
        result = nums[:]
        for root, indices in components.items():
            # Sort the indices within this component
            indices.sort()
            # Extract their corresponding values and sort them
            vals = [nums[i] for i in indices]
            vals.sort()
            # Place sorted values back in result at the sorted indices
            for i, v in zip(indices, vals):
                result[i] = v

        return result
