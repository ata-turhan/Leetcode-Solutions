from typing import List

class TrieNode:
    def __init__(self):
        # Each TrieNode contains a dictionary to hold child nodes (digits)
        self.children = {}

class Trie:
    def __init__(self):
        # The Trie has a root node that is initially empty
        self.root = TrieNode()

    def add(self, number: int):
        # Convert the number to a string so we can process its digits
        number_str = str(number)
        current_node = self.root
        for digit in number_str:
            # If the current digit is not already a child, create a new TrieNode
            if digit not in current_node.children:
                current_node.children[digit] = TrieNode()
            current_node = current_node.children[digit]

    def search(self, number: int) -> int:
        # Convert the number to a string for digit-by-digit comparison
        number_str = str(number)
        current_node = self.root
        matched_prefix_length = 0
        # Traverse the Trie, counting the length of the matched prefix
        for digit in number_str:
            if digit in current_node.children:
                matched_prefix_length += 1
                current_node = current_node.children[digit]
            else:
                break  # Stop if the digit does not match in the Trie
        return matched_prefix_length


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Build a Trie with all the numbers from arr2
        trie = Trie()
        for number in arr2:
            trie.add(number)

        max_prefix_length = 0
        # Search for the longest common prefix of each number in arr1 in the Trie
        for number in arr1:
            longest_prefix = trie.search(number)
            max_prefix_length = max(max_prefix_length, longest_prefix)

        return max_prefix_length
