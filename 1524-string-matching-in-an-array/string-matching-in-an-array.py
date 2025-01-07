class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = set()
        for word in words:
            for i in range(len(word)):
                for j in range(i, len(word)):
                    if i == 0 and j == len(word) - 1:
                        continue
                    substrings.add(word[i:j+1])

        res = []
        for word in words:
            if word in substrings:
                res.append(word)

        return res
        