class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]  # Initialize dp array

        for i in range(len1 - 1, -1, -1):  # Iterate over text1 in reverse
            for j in range(len2 - 1, -1, -1):  # Iterate over text2 in reverse
                if text1[i] == text2[j]:  # If characters match
                    dp[i][j] = dp[i + 1][j + 1] + 1  # Increment LCS length
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])  # Take the max of skipping either character

        return dp[0][0]  # Return the length of the longest common subsequence
