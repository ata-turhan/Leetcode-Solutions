class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        n = len(robot)
        m = len(factory)
        robot.sort()
        factory.sort()
        dp = [[float('inf')] * (m+1) for _ in range(n+1)]
        dp[0][0] = 0

        for i in range(n+1):
            dp[i][0] = float('inf')
        dp[0][0] = 0

        for j in range(1, m+1):
            dp[0][j] = 0  # No robots to assign

        for j in range(1, m+1):
            positionj, limitj = factory[j-1]
            for i in range(1, n+1):
                # Option 1: Not using factory j
                dp[i][j] = dp[i][j-1]
                # Option 2: Assigning k robots to factory j
                cost = 0
                for k in range(1, min(limitj, i)+1):
                    cost += abs(robot[i-k] - positionj)
                    if dp[i-k][j-1] + cost < dp[i][j]:
                        dp[i][j] = dp[i-k][j-1] + cost
        return dp[n][m]
