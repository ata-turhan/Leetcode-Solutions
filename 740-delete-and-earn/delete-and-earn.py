class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter= Counter(nums)
        houses = list(sorted(counter.keys()))
        dp = [0] * (len(houses)+1)
        dp[1] = counter[houses[0]] * houses[0]

        for i, house in enumerate(houses[1:], start=2):
            if house - 1 == houses[i-2]:
                dp[i] = max(dp[i-1], counter[house] * house + dp[i-2])
            else:
                dp[i] = dp[i-1] + counter[house] * house

        return dp[-1]
        