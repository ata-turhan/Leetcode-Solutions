class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = []

        for word in words:
            if word[0] in "aeiou" and word[-1] in "aeiou":
                vowels.append(1)
            else:
                vowels.append(0)

        prefix = [0]

        for vowel in vowels:
            prefix.append(prefix[-1] + vowel)


        res = []
        for q in queries:
            start, end = q
            res.append(prefix[end + 1] - prefix[start])

        return res
        