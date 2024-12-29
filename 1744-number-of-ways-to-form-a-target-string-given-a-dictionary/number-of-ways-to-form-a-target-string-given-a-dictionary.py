from functools import lru_cache

class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        MOD = 10**9 + 7
        # Precompute character frequencies at each position
        char_frequency = [[0] * 26 for _ in range(len(words[0]))]

        for word in words:
            for j, char in enumerate(word):
                char_frequency[j][ord(char) - 97] += 1

        @lru_cache(None)
        def get_words(words_index: int, target_index: int) -> int:
            if target_index == len(target):
                return 1
            if (
                words_index == len(words[0])
                or len(words[0]) - words_index < len(target) - target_index
            ):
                return 0

            count_ways = 0
            cur_pos = ord(target[target_index]) - 97
            # Don't match any character of target with any word.
            count_ways += get_words(words_index + 1, target_index)
            # Multiply the number of choices with getWords and add it to count.
            count_ways += (
                char_frequency[words_index][cur_pos]
                * get_words(words_index + 1, target_index + 1)
            )

            return count_ways % MOD

        return get_words(0, 0)
