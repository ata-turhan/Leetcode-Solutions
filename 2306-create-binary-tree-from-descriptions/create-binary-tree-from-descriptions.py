# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = dict()
        childs = set()

        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(val = parent)
            if child not in nodes:
                nodes[child] = TreeNode(val = child)
            childs.add(child)
            if isLeft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        for parent, child, isLeft in descriptions:
            if parent not in childs:
                root = parent
                break

        return nodes[root]

        