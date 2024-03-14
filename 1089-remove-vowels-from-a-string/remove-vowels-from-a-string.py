class Solution:
    def removeVowels(self, s: str) -> str:
        res = []
        for char in s:
            if char not in "aeiou":
                res.append(char)
        return "".join(res)
        