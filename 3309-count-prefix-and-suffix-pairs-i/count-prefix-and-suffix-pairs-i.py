class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """
        Count the number of pairs where one word is both a prefix and a suffix of another.

        :param words: List[str] - List of words to check.
        :return: int - Number of valid prefix-suffix pairs.
        """
        pair_count = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                word_length = len(words[i])
                # Check if words[i] is both a prefix and a suffix of words[j]
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    pair_count += 1

        return pair_count
