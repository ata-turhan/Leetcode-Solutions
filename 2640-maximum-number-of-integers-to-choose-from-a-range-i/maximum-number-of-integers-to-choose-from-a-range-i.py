class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        current_sum = 0
        banned_set = set(banned)
        count = 0

        for number in range(1, n + 1):
            if number not in banned_set:
                current_sum += number
                if current_sum > maxSum:
                    return count
                count += 1

        return count
