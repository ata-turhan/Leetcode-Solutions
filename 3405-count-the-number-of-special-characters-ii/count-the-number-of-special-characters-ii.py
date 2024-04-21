from collections import defaultdict

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Initialize dictionaries to store the last index of each lowercase and corresponding uppercase letter encountered in the word
        last_small_letter_index = defaultdict(int)
        last_large_letter_index = defaultdict(lambda: -1)
        
        # Iterate through each character in the word
        for i, letter in enumerate(word):
            # Check if the character is lowercase
            if letter.islower():
                # Update the last index of the lowercase letter in the small_letters dictionary
                last_small_letter_index[letter] = i
            else:
                # Update the last index of the lowercase equivalent of the uppercase letter in the large_letters dictionary
                if last_large_letter_index[letter.lower()] == -1:
                    last_large_letter_index[letter.lower()] = i
        
        # Initialize a variable to count the number of special characters
        special_char_count = 0
        
        # Iterate through each lowercase letter and check if it has a corresponding uppercase letter with a smaller index
        for letter in last_small_letter_index:
            if letter in last_large_letter_index and last_small_letter_index[letter] < last_large_letter_index[letter]:
                special_char_count += 1
        
        # Return the count of special characters
        return special_char_count
