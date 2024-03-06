# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(root, column_map, row, column):
            if not root: 
                return

            column_map[column].append((row, root.val))
            traverse(root.left, column_map, row + 1, column - 1)
            traverse(root.right, column_map, row + 1, column + 1)


        if not root:
            return []

        column_map = defaultdict(list)
        traverse(root, column_map, 0, 0)

        result = []
        for column in sorted(column_map.keys()):
            column_values = [value for row, value in sorted(column_map[column])]
            result.append(column_values)

        return result
        