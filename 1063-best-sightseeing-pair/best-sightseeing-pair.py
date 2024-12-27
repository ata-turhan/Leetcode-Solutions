class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_pair = (0, values[0])
        max_score = 0

        for i, val in enumerate(values[1:], start=1):
            score = best_pair[1] + val + best_pair[0] - i
            max_score = max(max_score, score)
            if (i + val) > sum(best_pair):
                best_pair = (i, val)

        return max_score
        