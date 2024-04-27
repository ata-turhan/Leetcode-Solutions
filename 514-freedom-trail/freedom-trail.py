class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def min_dist(total_len, idx1, idx2):
            dist1 = abs(idx1 - idx2)
            dist2 = total_len - dist1
            return min(dist1, dist2)

        @cache
        def dfs(ring, key, ring_idx, key_idx):
            if key_idx == len(key):
                return 0
            min_val = float("inf")
            for i in range(len(ring)):
                if ring[i] == key[key_idx]:
                    min_val = min(min_val, min_dist(len(ring), ring_idx, i) + 1 + dfs(ring, key, i, key_idx+1))
            return min_val
        return dfs(ring, key, 0, 0)
        