class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        idx = 0
        for char in str1:
            if char == str2[idx] or (chr((ord(char) - ord("a") + 1) % 26 + ord("a")) == str2[idx]):
                idx += 1
                if idx == len(str2):
                    break

        return idx == len(str2)
        