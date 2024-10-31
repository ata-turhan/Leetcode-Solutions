class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        n = len(robot)      # Number of robots
        m = len(factory)    # Number of factories
        
        robot.sort()        # Sort robot positions for optimal alignment
        factory.sort()      # Sort factories by position for the same reason
        
        # Initialize DP table where dp[i][j] represents the minimum total distance
        # to assign the first i robots to the first j factories
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        
        # Base case: No robots assigned to any factories results in zero total distance
        dp[0][0] = 0
        
        # If we have robots but no factories, it's impossible to assign them
        for i in range(1, n + 1):
            dp[i][0] = float('inf')
        
        # If we have factories but no robots, total distance is zero (nothing to assign)
        for j in range(1, m + 1):
            dp[0][j] = 0
        
        # Iterate over each factory
        for j in range(1, m + 1):
            positionj, limitj = factory[j - 1]  # Position and capacity of current factory
            
            # Iterate over the number of robots
            for i in range(1, n + 1):
                # Option 1: Do not assign any robots to the current factory
                dp[i][j] = dp[i][j - 1]
                
                # Option 2: Assign k robots to the current factory, where k ranges from 1 to the
                # minimum of the factory's capacity and the number of robots available
                cost = 0  # Initialize the cost for assigning k robots to factory j
                
                # Try all possible numbers of robots that can be assigned to the current factory
                for k in range(1, min(limitj, i) + 1):
                    # Calculate the cost incrementally by adding the distance of the robot being assigned
                    cost += abs(robot[i - k] - positionj)
                    
                    # Update dp[i][j] if assigning these k robots results in a lower total distance
                    dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + cost)
        
        # The answer is the minimum total distance to assign all n robots to m factories
        return dp[n][m]
