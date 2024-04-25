class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        res = 0
        for i in range(len(s)):
            cur_ord = ord(s[i]) - 97
            new_val = 1
            for j in range(26):
                if abs(j - cur_ord) <= k:
                    new_val = max(new_val, 1 + dp[j])
            dp[cur_ord] = max(dp[cur_ord], new_val)
        return max(dp)
        