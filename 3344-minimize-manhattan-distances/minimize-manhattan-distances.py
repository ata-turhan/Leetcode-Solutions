class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        # Find the maximum Manhattan distance between any two points
        _, i, j = self.max_man_dist(points)
        
        # Find the maximum Manhattan distances after removing one of the points
        max_dist1, _, _ = self.max_man_dist(points[:i] + points[i+1:])
        max_dist2, _, _ = self.max_man_dist(points[:j] + points[j+1:])
        
        # Return the minimum of the two maximum distances
        return min(max_dist1, max_dist2)
            
    def max_man_dist(self, points):
        # Calculate the sums and differences of x and y coordinates for all points
        sums = [p[0] + p[1] for p in points]
        diffs = [p[0] - p[1] for p in points]

        # Find the maximum and minimum sums and their corresponding indices
        max_sum = max(sums)
        max_sum_idx = sums.index(max_sum)
        min_sum = min(sums)
        min_sum_idx = sums.index(min_sum)
        abs_sums = max_sum - min_sum

        # Find the maximum and minimum differences and their corresponding indices
        max_diff = max(diffs)
        max_diff_idx = diffs.index(max_diff)
        min_diff = min(diffs)
        min_diff_idx = diffs.index(min_diff)
        abs_diffs = max_diff - min_diff

        # Determine whether to return the maximum sums or differences
        if abs_sums > abs_diffs:
            return abs_sums, max_sum_idx, min_sum_idx
        else:
            return abs_diffs, max_diff_idx, min_diff_idx
