class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict = set(wordDict)

        def backtrack(i, j, array):
            if j == len(s)-1:
                if s[i:j+1] in wordDict:
                    array.append(s[i:j+1])
                    res.append(" ".join(array))
                    array.pop()
                return
            if s[i:j+1] in wordDict:
                array.append(s[i:j+1])
                backtrack(j+1, j+1, array)
                array.pop()
                backtrack(i, j+1, array)
            else:
                backtrack(i, j+1, array)

        backtrack(0, 0, [])
        return res

            