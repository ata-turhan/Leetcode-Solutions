class TrieNode:
    """Node for Trie data structure."""
    def __init__(self):
        """Initialize a TrieNode."""
        self.children = {}
        self.value = 0
        self.is_word = False

class MapSum:
    """MapSum class to store key-value pairs and calculate the sum of values for a given prefix."""
    def __init__(self):
        """Initialize a MapSum object with an empty root TrieNode."""
        self.root = TrieNode()

    def insert(self, key: str, value: int) -> None:
        """Insert a key-value pair into the MapSum."""
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.value = value
        node.is_word = True

    def sum(self, prefix: str) -> int:
        """Return the sum of values for keys starting with the given prefix."""
        node = self.root
        # Traverse the Trie based on the prefix
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return 0
        # Calculate the sum starting from the node corresponding to the prefix
        return self._calculate_sum(node)

    def _calculate_sum(self, node: TrieNode) -> int:
        """Recursively calculate the sum of values starting from the given node."""
        total_sum = node.value if node.is_word else 0
        for child_node in node.children.values():
            total_sum += self._calculate_sum(child_node)
        return total_sum


# Example usage:
# obj = MapSum()
# obj.insert(key, value)
# param_2 = obj.sum(prefix)
