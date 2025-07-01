class Solution:
    def possibleStringCount(self, word: str) -> int:
        freqs = []
        cur_freq = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                cur_freq += 1
            else:
                freqs.append(cur_freq)
                cur_freq = 1

        freqs.append(cur_freq)

        return sum(val - 1 for val in freqs) + 1
        