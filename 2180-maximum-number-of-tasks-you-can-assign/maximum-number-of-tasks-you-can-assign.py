from typing import List
from bisect import bisect_left

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)

        class DSU:
            def __init__(self, size: int):
                self.parent = list(range(size))
            def find(self, x: int) -> int:
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x
            def union(self, x: int, y: int) -> None:
                rx = self.find(x)
                ry = self.find(y)
                self.parent[rx] = ry

        def can(k: int) -> bool:
            if k == 0:
                return True
            tasks_k = tasks[:k]
            workers_k = workers[m - k:]
            dsu_fwd = DSU(k + 1)
            dsu_rev = DSU(k + 1)
            pills_left = pills

            for t in reversed(tasks_k):
                # Try unboosted: use the strongest available worker
                rev_idx = dsu_rev.find(0)
                if rev_idx < k:
                    i = k - 1 - rev_idx
                    if workers_k[i] >= t:
                        dsu_fwd.union(i, i + 1)
                        dsu_rev.union(rev_idx, rev_idx + 1)
                        continue
                # Otherwise, try boosting
                if pills_left == 0:
                    return False
                need = t - strength
                pos = bisect_left(workers_k, need)
                idx = dsu_fwd.find(pos)
                if idx >= k:
                    return False
                dsu_fwd.union(idx, idx + 1)
                dsu_rev.union(k - 1 - idx, k - idx)
                pills_left -= 1
            return True

        lo, hi = 0, min(n, m)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
