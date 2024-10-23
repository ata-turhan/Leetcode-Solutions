# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        queue.append(root)
        level_sums = []

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level_sums.append(level_sum)

        level = 0
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            level_sum = level_sums[level+1]

            for _ in range(level_size):
                node = queue.popleft()

                sibling_sum = 0

                if node.left:
                    queue.append(node.left)
                    sibling_sum += node.left.val
                if node.right:
                    queue.append(node.right)
                    sibling_sum += node.right.val

                if level == 0:
                    node.val = 0
                
                if node.left:
                    node.left.val = level_sum - sibling_sum
                if node.right:
                    node.right.val = level_sum - sibling_sum
            
            level += 1
            if level == len(level_sums) - 1:
                break

        return root

        