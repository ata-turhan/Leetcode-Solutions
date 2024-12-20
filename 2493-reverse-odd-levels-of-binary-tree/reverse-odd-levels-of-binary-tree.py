# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])
        level = 0
        level_nodes = []

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if level % 2 == 1:
                    level_nodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_nodes:
                for i in range(len(level_nodes)//2):
                    left_node = level_nodes[i]
                    right_node = level_nodes[-i-1]
                    left_node.val, right_node.val = right_node.val, left_node.val

                level_nodes = []

            level += 1

        return root
