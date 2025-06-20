class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        n_count, s_count, e_count, w_count = 0, 0, 0, 0
        max_dist = 0

        for char in s:
            if char == "N":
                n_count += 1
            if char == "S":
                s_count += 1
            if char == "E":
                e_count += 1
            if char == "W":
                w_count += 1

            dist = abs(n_count - s_count) + abs(e_count - w_count)
            min_vals = min(n_count, s_count) + min(e_count, w_count)
            increment = min(k, min_vals)

            max_dist = max(max_dist, dist + 2 * increment)

        return max_dist
            

        
            