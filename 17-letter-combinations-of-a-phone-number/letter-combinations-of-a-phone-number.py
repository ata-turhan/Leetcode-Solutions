from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Base case: if the input digits is empty, return an empty list
        if not digits:
            return []
        
        # Initialize a set with an empty string to store combinations
        combinations = set([""])
        
        # Dictionary mapping each digit to its corresponding letters
        digit_to_letters = {
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'], 
            '4': ['g', 'h', 'i'], 
            '5': ['j', 'k', 'l'], 
            '6': ['m', 'n', 'o'], 
            '7': ['p', 'q', 'r', 's'], 
            '8': ['t', 'u', 'v'], 
            '9': ['w', 'x', 'y', 'z']
        }
        
        # Iterate over each digit in the input
        for digit in digits:
            # Get the letters corresponding to the current digit
            letters = digit_to_letters[digit]
            # Create a new set to store updated combinations
            new_combinations = set()
            # Iterate over each existing combination
            for combination in combinations:
                # Append each letter to the existing combinations and add to the new set
                for letter in letters:
                    new_combinations.add(combination + letter)
            # Update the combinations set with the new combinations
            combinations = new_combinations
        
        return list(combinations)
