from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Convert the dictionary to a set for O(1) lookups
        word_set = set(dictionary)
        n = len(s)
        
        # Initialize dp array where dp[i] is the minimum number of extra characters for first i characters
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # No characters, no extra characters
        
        # Iterate through each position in the string s
        for i in range(1, n + 1):
            # Try to find if there's a valid word ending at position i-1
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])
            # Always consider leaving the last character as extra if no valid word is found
            dp[i] = min(dp[i], dp[i - 1] + 1)
        
        # The result will be stored in dp[n], which gives the minimum extra characters for the entire string
        return dp[n]
