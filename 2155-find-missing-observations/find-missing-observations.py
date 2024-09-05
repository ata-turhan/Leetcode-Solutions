class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_m = sum(rolls)
        len_m = len(rolls)
        total_sum = mean * (n + len_m)
        sum_n = total_sum - sum_m
        min_sum_n = 1 * n
        max_sum_n = 6 * n
        if not ( min_sum_n <= sum_n <= max_sum_n):
            return []
        if (sum_n + sum_m) % (len_m + n) != 0:
            return []

        mean_n = math.floor(sum_n / n)
        arr_n = [mean_n] * n
        sum_arr = mean_n * n
        extras = sum_n - sum_arr

        for i in range(extras):
            arr_n[i] += 1

        return arr_n

        