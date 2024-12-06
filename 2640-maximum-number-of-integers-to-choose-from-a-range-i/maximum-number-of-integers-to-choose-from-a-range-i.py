class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        cur_sum = 0
        set_banned = set(banned)
        num_count = 0
        
        for i in range(1, n+1):
            if i not in set_banned:
                cur_sum += i
                if cur_sum > maxSum:
                    return num_count
                else:
                    num_count += 1

        return num_count
        