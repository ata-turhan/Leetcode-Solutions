class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Count the frequency of each number in nums
        counter = Counter(nums)
        # Get the sorted list of unique numbers
        houses = list(sorted(counter.keys()))
        # Initialize dp array with an extra space for easier indexing
        dp = [0] * (len(houses) + 1)
        # Initialize the first element in dp array
        dp[1] = counter[houses[0]] * houses[0]

        # Iterate through the sorted list of unique numbers starting from the second element
        for i, house in enumerate(houses[1:], start=2):
            # If the current number is consecutive to the previous one
            if house - 1 == houses[i - 2]:
                # Take the maximum of either not taking the current number or taking it
                dp[i] = max(dp[i - 1], counter[house] * house + dp[i - 2])
            else:
                # If not consecutive, add the current number's total to the previous total
                dp[i] = dp[i - 1] + counter[house] * house

        # Return the last element in dp array which contains the maximum points
        return dp[-1]
