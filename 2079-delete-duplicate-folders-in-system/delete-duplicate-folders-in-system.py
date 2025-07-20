from typing import List
from collections import Counter

class Solution:
    class _Node:
        __slots__ = ('children', 'sig_id')
        def __init__(self):
            self.children = {}
            self.sig_id = 0

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # 1) Build the folder trie
        root = Solution._Node()
        for path in paths:
            curr = root
            for folder in path:
                curr = curr.children.setdefault(folder, Solution._Node())

        # 2) Assign subtree signature IDs (post-order) and count duplicates
        subtree_map = {}        # Maps subtree structure tuple -> unique ID
        count = Counter()       # Counts occurrences of each subtree ID
        id_counter = [1]        # Mutable counter for assigning new IDs

        def dfs(node: Solution._Node) -> int:
            if not node.children:
                return 0  # Leaf nodes get signature ID 0 (ignored for duplication)
            items = []
            for name in sorted(node.children):
                child = node.children[name]
                cid = dfs(child)
                items.append((name, cid))
            key = tuple(items)
            if key not in subtree_map:
                subtree_map[key] = id_counter[0]
                id_counter[0] += 1
            sid = subtree_map[key]
            count[sid] += 1
            node.sig_id = sid
            return sid

        dfs(root)

        # 3&4) Traverse again to collect non-deleted folder paths
        result: List[List[str]] = []
        def collect(node: Solution._Node, path: List[str], deleted: bool):
            if deleted:
                return
            for name, child in node.children.items():
                is_dup = (child.sig_id != 0 and count[child.sig_id] > 1)
                if not is_dup:
                    result.append(path + [name])
                collect(child, path + [name], is_dup)

        collect(root, [], False)
        return result
