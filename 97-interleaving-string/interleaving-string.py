class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Check if the lengths of s1 and s2 add up to the length of s3
        if len(s1) + len(s2) != len(s3):
            return False

        # Initialize the DP table with False values
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True  # Base case: empty s1 and s2 form empty s3

        # Fill the DP table from the end to the beginning
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                # Check if the current character of s1 matches with the corresponding character in s3
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                # Check if the current character of s2 matches with the corresponding character in s3
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        
        return dp[0][0]  # Return the result of interleaving s1 and s2 to form s3
