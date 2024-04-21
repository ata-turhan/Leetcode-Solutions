class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Initialize sets to store lowercase and corresponding uppercase letters encountered in the word
        lowercase_letters = set()
        uppercase_letters = set()
        
        # Iterate through each character in the word
        for char in word:
            # Check if the character is lowercase
            if char.islower():
                # Add the lowercase character to the lowercase set
                lowercase_letters.add(char)
            else:
                # Add the lowercase equivalent of the uppercase character to the uppercase set
                uppercase_letters.add(char.lower())
        
        # Initialize a variable to count the number of special characters
        special_char_count = 0
        
        # Iterate through each lowercase letter
        for letter in lowercase_letters:
            # If the lowercase letter has a corresponding uppercase letter, increment the special character count
            if letter in uppercase_letters:
                special_char_count += 1
        
        # Return the count of special characters
        return special_char_count
