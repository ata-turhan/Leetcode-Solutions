class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        cum_sum, min_sum, max_sum = 0, 0, 0

        for diff in differences:
            cum_sum += diff
            min_sum = min(min_sum, cum_sum)
            max_sum = max(max_sum, cum_sum)

        min_val = lower + abs(min_sum)
        max_val = upper - abs(max_sum)

        if min_val > max_val:
            return 0
        else:
            return max_val - min_val + 1