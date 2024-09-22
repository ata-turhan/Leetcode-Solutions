from typing import List
from math import isqrt

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Helper function to check if workers can finish in a given time T
        def canFinishInTime(T: int) -> bool:
            totalReduction = 0
            for W in workerTimes:
                # Calculate S = (2 * T) // W to avoid floating point errors
                S = (2 * T) // W
                # Discriminant D = 1 + 4S
                D = 1 + 4 * S
                # Compute integer square root of D
                sqrt_D = isqrt(D)
                # Calculate maximum x using the quadratic formula
                x = (sqrt_D - 1) // 2
                if x > 0:
                    totalReduction += x
                if totalReduction >= mountainHeight:
                    return True
            return False

        left = 1
        # Set an upper bound for right based on the maximum possible time
        right = mountainHeight * (mountainHeight + 1) // 2 * max(workerTimes)

        # Perform binary search to find the minimum time
        while left < right:
            mid = (left + right) // 2
            if canFinishInTime(mid):
                right = mid
            else:
                left = mid + 1

        return left
