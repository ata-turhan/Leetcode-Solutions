class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split the string by whitespace
        words = re.split(r"\s+", s)

        # Determine the index of the last word
        last_word_idx = -1 if words[-1] else -2

        # Return the length of the last word
        return len(words[last_word_idx])
        