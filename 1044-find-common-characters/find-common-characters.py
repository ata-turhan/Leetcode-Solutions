from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
        Finds the common characters in all words and returns them as a list.
        
        :param words: List[str] - A list of strings.
        :return: List[str] - A list of common characters.
        """
        total_counter = Counter(words[0])  # Initialize the counter with the first word

        # Iterate through each word and update the total counter
        for word in words[1:]:
            word_counter = Counter(word)  # Create a counter for the current word
            total_counter &= word_counter  # Perform an intersection with the total counter

        res = []  # Initialize the result list

        # Add the common characters to the result list based on their counts
        for char, count in total_counter.items():
            res.extend([char] * count)

        return res  # Return the list of common characters

# Example usage:
# sol = Solution()
# print(sol.commonChars(["bella", "label", "roller"]))  # Output: ['e', 'l', 'l']
# print(sol.commonChars(["cool", "lock", "cook"]))     # Output: ['c', 'o']
