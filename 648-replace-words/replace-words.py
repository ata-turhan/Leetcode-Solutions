class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_word = False  # Flag to indicate if the node represents the end of a word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Build the trie from the dictionary words
        root = TrieNode()
        for word in dictionary:
            self.insert(root, word)

        # Split the sentence into words and replace them if a prefix is found
        words = sentence.split()
        for i, word in enumerate(words):
            prefix = self.find_prefix(root, word)
            if prefix:
                words[i] = prefix

        # Join the modified words back into a sentence
        return ' '.join(words)

    def insert(self, root, word):
        # Insert a word into the trie
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True  # Mark the end of the word

    def find_prefix(self, root, word):
        # Find the shortest prefix of a word that is present in the trie
        node = root
        prefix = []
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            prefix.append(char)
            if node.is_word:
                return ''.join(prefix)  # Return the prefix if a word ends here
        return None  # Return none if no prefix is found
