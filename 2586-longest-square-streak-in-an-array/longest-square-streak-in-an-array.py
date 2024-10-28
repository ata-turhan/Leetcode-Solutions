class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        counter = Counter(nums)
        longest_streak = 0
        for num in counter:
            cur_streak = 0
            while num in counter:
                cur_streak += 1
                num **= 2
            longest_streak = max(longest_streak, cur_streak)

        return longest_streak if longest_streak > 1 else -1


        