class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_letters = set(allowed)
        consistent_strs = 0
        for word in words:
            for letter in word:
                if letter not in allowed_letters:
                    break
            else:
                consistent_strs += 1
        return consistent_strs
        