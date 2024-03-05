class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s)-1
        while l < r and s[l] == s[r]:
            letter = s[l]
            while l < len(s) and letter == s[l]:
                l += 1
            while l < r and letter == s[r]:
                r -= 1
        return r-l+1