class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        covered = 0
        for char in s:
            if char == t[covered]:
                covered += 1
                if covered == len(t):
                    break

        return len(t) - covered
        