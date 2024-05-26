class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]

        
        def create(i, absents, consec_lates):
            if dp[i][absents][consec_lates] != -1:
                return dp[i][absents][consec_lates]

            if i == n:
                return 1
            
            res = 0

            if absents == 0:
                res += create(i+1, absents+1, 0) % (10**9 + 7)
            
            res += create(i+1, absents, 0) % (10**9 + 7)

            if consec_lates < 2:
                res += create(i+1, absents, consec_lates+1) % (10**9 + 7)

            dp[i][absents][consec_lates] = res % (10**9 + 7)
            return res % (10**9 + 7)

        return create(0, 0, 0)

