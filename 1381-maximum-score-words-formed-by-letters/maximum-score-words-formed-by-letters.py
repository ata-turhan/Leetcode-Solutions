from typing import List
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Create a dictionary to map each character to its score
        char_scores = {chr(ord('a') + i): s for i, s in enumerate(score)}

        def backtrack(index: int, remaining_letters: Counter, current_score: int) -> int:
            # Base case: If we have considered all words
            if index == len(words):
                return current_score

            max_score = 0

            # Try including the current word
            temp_letters = remaining_letters.copy()
            word_score = 0

            for char in words[index]:
                if temp_letters[char] == 0:
                    break
                else:
                    temp_letters[char] -= 1
                    word_score += char_scores[char]
            else:
                max_score = max(max_score, backtrack(index + 1, temp_letters, current_score + word_score))

            # Try excluding the current word
            max_score = max(max_score, backtrack(index + 1, remaining_letters, current_score))

            return max_score

        # Initialize remaining letters as a Counter
        remaining_letters = Counter(letters)
        # Start the backtracking process from the first word
        return backtrack(0, remaining_letters, 0)

# Example usage:
# sol = Solution()
# words = ["dog", "cat", "dad", "good"]
# letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
# score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# print(sol.maxScoreWords(words, letters, score))  # Output should be 23
