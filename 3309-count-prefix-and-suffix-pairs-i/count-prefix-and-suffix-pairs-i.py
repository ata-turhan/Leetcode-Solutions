class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                word_len = len(words[i])
                if words[j][:word_len] == words[i] and words[j][-word_len:] == words[i]:
                    count += 1

        return count