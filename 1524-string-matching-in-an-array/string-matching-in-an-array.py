class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        Finds all words in the list that are substrings of other words in the list.

        :param words: List of strings.
        :return: List of words that are substrings of other words.
        """
        # Set to store all substrings found across the words
        substring_set = set()
        
        # Collect all substrings from the words
        for word in words:
            for start_idx in range(len(word)):
                for end_idx in range(start_idx, len(word)):
                    # Skip adding the entire word itself to the substring set
                    if start_idx == 0 and end_idx == len(word) - 1:
                        continue
                    # Add substring [start_idx:end_idx+1] to the set
                    substring_set.add(word[start_idx:end_idx+1])

        # List to store results for words that are found in the substring set
        result = []
        for word in words:
            if word in substring_set:  # Check if the current word is a substring of any word
                result.append(word)

        return result
