from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.word_indices = []  # List to store indices of words with the same prefix

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.words = words  # Store the list of words
        self.N = len(words[0])  # Length of each word
        self.buildTrie()  # Build the trie from the list of words

        results = []  # List to store word squares
        for word in words:
            word_square = [word]  # Initialize word square with current word
            self.backtracking(1, word_square, results)  # Perform backtracking to find word squares
        return results

    def buildTrie(self):
        self.trie = TrieNode()  # Initialize the root of the trie
        for wordIndex, word in enumerate(self.words):
            node = self.trie
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()  # Create a new node if character not present
                node = node.children[char]
                node.word_indices.append(wordIndex)  # Append index of word to node

    def backtracking(self, step, word_square, results):
        if step == self.N:
            results.append(word_square[:])  # Add word square to results when completed
            return

        prefix = ''.join([word[step] for word in word_square])  # Get prefix for next word
        for word_index in self.getWordsWithPrefix(prefix):
            word_square.append(self.words[word_index])  # Add word with matching prefix
            self.backtracking(step+1, word_square, results)  # Recursively find next word
            word_square.pop()  # Remove last word to backtrack

    def getWordsWithPrefix(self, prefix):
        node = self.trie
        for char in prefix:
            if char not in node.children:
                return []  # Return empty list if prefix not found
            node = node.children[char]
        return node.word_indices  # Return indices of words with matching prefix
