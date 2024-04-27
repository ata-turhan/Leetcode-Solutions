from functools import cache

class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        """
        Calculate the number of distinct ways to climb to the top of the stairs.

        Args:
            n (int): The number of stairs.

        Returns:
            int: The number of distinct ways to climb to the top.
        """
        # Base cases: 0 stairs (0 ways), 1 stair (1 way), 2 stairs (2 ways)
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Dynamic programming approach
        # Initialize variables to store the number of ways to climb to the current step
        step1 = 0  # Represents the number of ways to reach step n-1
        step2 = 1  # Represents the number of ways to reach step n-2
        
        # Iterate through each step from 1 to n
        for _ in range(n):
            # Calculate the number of ways to reach the next step
            # by summing the number of ways to reach the current step (step2)
            # and the number of ways to reach the step before the current step (step1)
            step1, step2 = step2, step1 + step2
        
        # Return the number of ways to reach the top step (step2)
        return step2
