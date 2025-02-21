# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        def dfs(node):
            if node.left:
                node.left.val = 2 * node.val + 1
                self.nodes.add(node.left.val)
                dfs(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                self.nodes.add(node.right.val)
                dfs(node.right)

        root.val = 0
        self.nodes = set()
        self.nodes.add(root.val)
        dfs(root)
        

    def find(self, target: int) -> bool:
        return target in self.nodes


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)