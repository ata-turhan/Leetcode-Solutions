# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}  # Dictionary to store all the nodes
        children = set()  # Set to keep track of all child nodes

        # Process each description to build the tree
        for parent_val, child_val, is_left in descriptions:
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(val=parent_val)
            if child_val not in nodes:
                nodes[child_val] = TreeNode(val=child_val)
            
            children.add(child_val)
            
            if is_left:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]

        # The root node is the one that is never a child node
        for parent_val, child_val, is_left in descriptions:
            if parent_val not in children:
                root_val = parent_val
                break

        return nodes[root_val]
