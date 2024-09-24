class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, number):
        str_number = str(number)
        cur = self.root
        for char in str_number:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]

    def search(self, number):
        str_number = str(number)
        count = 0
        cur = self.root
        for char in str_number:
            if char in cur.children:
                count += 1
                cur = cur.children[char]
            else:
                break
        return count


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie2 = Trie()
        for int2 in arr2:
            trie2.add(int2)

        max_prefix_len = 0
        for int1 in arr1:
            longest_prefix = trie2.search(int1)
            max_prefix_len = max(max_prefix_len, longest_prefix)

        return max_prefix_len

        
        