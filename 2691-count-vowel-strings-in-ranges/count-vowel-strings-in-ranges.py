class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        """
        Count the number of words that start and end with a vowel in specified ranges.

        :param words: List of words to analyze.
        :param queries: List of [start, end] ranges to query.
        :return: List of counts for each query.
        """
        # Step 1: Mark words that start and end with vowels
        is_vowel_word = []
        vowels = {"a", "e", "i", "o", "u"}

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                is_vowel_word.append(1)  # Mark as a vowel word
            else:
                is_vowel_word.append(0)  # Not a vowel word

        # Step 2: Build prefix sum array for efficient range queries
        prefix_sum = [0]
        for is_vowel in is_vowel_word:
            prefix_sum.append(prefix_sum[-1] + is_vowel)

        # Step 3: Process each query to count vowel words in the range
        result = []
        for start_idx, end_idx in queries:
            # Use prefix sums to calculate the count in O(1)
            result.append(prefix_sum[end_idx + 1] - prefix_sum[start_idx])

        return result
