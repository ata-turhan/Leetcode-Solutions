from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        backward, res = {}, []  # Initialize a dictionary to store reversed words and a list to store results
        for i, word in enumerate(words):
            backward[word[::-1]] = i  # Store the index of reversed word in the dictionary

        for i, word in enumerate(words):
            if word in backward and backward[word] != i:
                res.append([i, backward[word]])  # Check for exact palindromes

            if word != "" and "" in backward and word == word[::-1]:
                res.append([i, backward[""]])  # Check for empty string and its reverse
                res.append([backward[""], i])

            for j in range(len(word)):
                if word[j:] in backward and word[:j] == word[j-1::-1]:
                    res.append([backward[word[j:]], i])  # Check for suffix palindromes
                if word[:j] in backward and word[j:] == word[:j-1:-1]:
                    res.append([i, backward[word[:j]]])  # Check for prefix palindromes

        return res  # Return the list of palindrome pairs
