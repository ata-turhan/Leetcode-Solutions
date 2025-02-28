class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        # find the LCS of s1 and s2
        lcs = self.getLCS(s1, s2)
        i, j = 0, 0
        result = ""
        # merge s1 and s2 with the LCS
        for c in lcs:
            # add characters from s1 until the LCS character is found
            while s1[i] != c:
                result += s1[i]
                i += 1
            # add characters from s2 until the LCS character is found
            while s2[j] != c:
                result += s2[j]
                j += 1
            # add the LCS character
            result += c
            i += 1
            j += 1
        # add any remaining characters from s1 and s2
        result += s1[i:] + s2[j:]
        # return the merged string
        return result

    # helper method to find the LCS of two strings
    def getLCS(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        # fill the dp array using dynamic programming
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # backtrack from the bottom right corner of the dp array to find the LCS
        lcs = ""
        i, j = m, n
        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                lcs = s1[i-1] + lcs
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        return lcs