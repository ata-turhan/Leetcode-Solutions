class Solution:
    def isValid(self, word: str) -> bool:
        # Check if the word has at least 3 characters
        if len(word) < 3:
            return False

        # Define sets of vowels and consonants
        vowels = set('aeiouAEIOU')
        consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')

        # Initialize flags for checking vowels and consonants
        has_vowel = False
        has_consonant = False

        # Iterate through the characters in the word
        for char in word:
            if char in vowels:
                has_vowel = True
            elif char in consonants:
                has_consonant = True
            elif not (char.isdigit() or char.isalpha()):
                # Return False if the character is neither a digit nor an alphabet
                return False

        # Return True if the word contains both vowels and consonants
        return has_vowel and has_consonant
