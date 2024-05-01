class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find the index of the target character in the word
        index_of_ch = word.find(ch)
        # If the character is not found, return the original word
        if index_of_ch == -1:
            return word
        else:
            # Reverse the prefix of the word up to the target character
            reversed_prefix = word[:index_of_ch+1][::-1]
            # Concatenate the reversed prefix with the remaining part of the word
            return reversed_prefix + word[index_of_ch+1:]
