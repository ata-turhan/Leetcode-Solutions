class Solution:
    def possibleStringCount(self, word: str) -> int:
        total_combs = 1
        cur_freq = 1
        
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                cur_freq += 1
            else:
                total_combs += cur_freq - 1
                cur_freq = 1

        total_combs += cur_freq - 1

        return total_combs
        