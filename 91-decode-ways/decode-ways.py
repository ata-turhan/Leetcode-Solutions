class Solution:
    def numDecodings(self, s: str) -> int:
        # Dynamic Programming array to store the number of ways to decode the string
        dp = [0] * (len(s) + 1)
        # Base case: An empty string has one way to be decoded
        dp[len(s)] = 1

        # Iterate from the end of the string to the beginning
        for i in range(len(s) - 1, -1, -1):
            # If the current character is '0', there are no valid decodings
            if s[i] == "0":
                dp[i] = 0
            else:
                # Decode the current character as a single digit
                dp[i] = dp[i + 1]
                # Check if the next two characters form a valid two-digit number
                if i + 1 < len(s) and 0 < int(s[i:i + 2]) < 27:
                    dp[i] += dp[i + 2]

        return dp[0]
