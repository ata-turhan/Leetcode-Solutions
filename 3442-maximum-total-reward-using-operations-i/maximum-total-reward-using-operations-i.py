from typing import List
from functools import cache
from bisect import bisect_right

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues = list(set(rewardValues))
        rewardValues.sort()

        @cache
        def dp(index: int, totalReward: int) -> int:
            if index == len(rewardValues):
                return totalReward
            
            currentValue = rewardValues[index]
            
            if currentValue > totalReward:
                nextIndex = bisect_right(rewardValues, totalReward + currentValue)
                # Option 1: Include the current reward value
                include = dp(nextIndex, totalReward + currentValue)
                # Option 2: Skip the current reward value
                skip = dp(index + 1, totalReward)
                # Return the maximum of including or skipping the current reward value
                return max(include, skip)
            else:
                # Option: Skip the current reward value
                return dp(index + 1, totalReward)

        return dp(0, 0)
