class TrieNode():
    def __init__(self):
        self.children = {}
        self.val = 0
        self.is_word = False

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.val = val
        node.is_word = True
        

    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return 0
        def dfs(root):
            res = root.val if root.is_word else 0
            for child in root.children:
                res += dfs(root.children[child])
            return res
        return dfs(node)

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)