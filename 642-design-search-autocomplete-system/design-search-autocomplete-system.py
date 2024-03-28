class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.times = 0  # Number of times the sentence is typed
        self.is_sentence = False  # Flag to indicate if the node represents the end of a sentence

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()  # Initialize the root of the Trie
        self.prefix = ""  # Initialize the current prefix
        self.reset(sentences, times)  # Reset the Trie with the given sentences and times
        self.cur_node = self.root  # Initialize the current node to the root

    def reset(self, sentences, times):
        # Reset the Trie with the given sentences and times
        for sentence, time in zip(sentences, times):
            self.insert(sentence, time)

    def insert(self, sentence, time):
        # Insert a sentence into the Trie
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()  # Create a new node if the character is not in children
            node = node.children[char]
        node.is_sentence = True  # Mark the end of the sentence
        node.times += time  # Update the number of times the sentence is typed

    def input(self, c: str) -> List[str]:
        if c == "#":  # If the input character is '#', it means the sentence ends
            self.insert(self.prefix, 1)  # Insert the current sentence into the Trie with 1 count
            self.prefix = ""  # Reset the prefix for the next sentence
            self.cur_node = self.root  # Reset the current node to the root
            return []  # Return an empty list as the sentence is complete

        self.prefix += c  # Add the input character to the current prefix
        if c not in self.cur_node.children:
            self.cur_node.children[c] = TrieNode()  # Create a new node for the input character if not present
        self.cur_node = self.cur_node.children[c]  # Move to the next node in the Trie

        # Get the top 3 historical hot sentences with the same prefix
        suggestions = self.find_top_k_sentences(self.cur_node, 3)

        return suggestions

    def find_top_k_sentences(self, node, k):
        # Find the top k historical hot sentences with the same prefix
        heap = []
        self.dfs(node, self.prefix, heap)  # Perform depth-first search to find all sentences with the same prefix
        return [sentence for _, sentence in heapq.nsmallest(k, heap)]  # Return the top k sentences

    def dfs(self, node, path, heap):
        # Depth-first search to find all sentences with the same prefix
        if node.is_sentence:
            heapq.heappush(heap, (-node.times, path))  # Push the sentence to the heap with its count

        for char, child_node in node.children.items():
            self.dfs(child_node, path + char, heap)  # Recursively explore child nodes