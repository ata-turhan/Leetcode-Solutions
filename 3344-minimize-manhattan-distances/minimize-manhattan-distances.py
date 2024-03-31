class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        _, i, j = self.max_man_dist(points)
        max_dist1, _, _ = self.max_man_dist(points[:i] + points[i+1:])
        max_dist2, _, _ = self.max_man_dist(points[:j] + points[j+1:])
        return min(max_dist1, max_dist2)
            

    def man_dist(self, p1, p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


    def max_man_dist(self, points):
        sums = [p[0] + p[1] for p in points]
        diffs = [p[0] - p[1] for p in points]

        max_sum = max(sums)
        max_sum_idx = sums.index(max_sum)
        min_sum = min(sums)
        min_sum_idx = sums.index(min_sum)
        abs_sums = max_sum - min_sum

        max_diff = max(diffs)
        max_diff_idx = diffs.index(max_diff)
        min_diff = min(diffs)
        min_diff_idx = diffs.index(min_diff)
        abs_diffs = max_diff - min_diff

        if abs_sums > abs_diffs:
            return abs_sums, max_sum_idx, min_sum_idx
        else:
            return abs_diffs, max_diff_idx, min_diff_idx