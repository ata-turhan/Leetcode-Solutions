class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        total_counter = Counter(words[0])

        for word in words:
            word_counter = Counter(word)
            total_counter &= word_counter

        res = []
        print(total_counter)

        for key, val in total_counter.items():
            res.extend([key] * val)

        return res
        