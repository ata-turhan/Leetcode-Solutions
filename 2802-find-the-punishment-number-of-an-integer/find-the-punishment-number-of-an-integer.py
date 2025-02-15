class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_be_partitioned(num, sum_):
            def dfs(i, cur_sum, cur_num):
                if i == len(num):
                    return cur_sum + int(cur_num) == sum_
                elif cur_sum > sum_:
                    return False
                return dfs(i + 1, cur_sum, cur_num + num[i]) or dfs(i + 1, cur_sum + int(cur_num), num[i])

            return dfs(0, 0, "0")

        punishment_number = 0

        for num in range(1, n+1):
            if can_be_partitioned(str(num * num), num):
                print(num)
                punishment_number += num * num

        return punishment_number
        