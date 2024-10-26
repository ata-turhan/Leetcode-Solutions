# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # Step 1: Calculate height of each node using DFS
        height = {}  # Dictionary to store height of each node
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -1  # Base case: height of empty subtree is -1
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            node_height = 1 + max(left_height, right_height)
            height[node.val] = node_height
            return node_height

        
        
        dfs(root)  # Populate the height dictionary

        print(height)

        # Step 2: Calculate levels using BFS and create heaps for each level
        level = {}  # Dictionary to store level of each node
        level_heights = defaultdict(list)  # Dictionary of max-heaps for each level

        queue = deque([(root, 0)])  # (node, level)
        while queue:
            node, lvl = queue.popleft()
            level[node.val] = lvl
            heapq.heappush(level_heights[lvl], (-height[node.val], node.val))  # Store negative height for max-heap

            if node.left:
                queue.append((node.left, lvl + 1))
            if node.right:
                queue.append((node.right, lvl + 1))

        # Step 3: Process each query
        result = []
        for q in queries:
            node_level = level[q]
            node_height = height[q]

            max_height, node_of_max_height = heappop(level_heights[node_level])
            max_height = -max_height
            if max_height == node_height:
                if level_heights[node_level]:
                    second_max_height, second_node_of_max_height = heappop(level_heights[node_level])
                    max_height_after_removal = -second_max_height
                    heappush(level_heights[node_level], (second_max_height, second_node_of_max_height))
                    heappush(level_heights[node_level], (-max_height, node_of_max_height))
                else:
                    max_height_after_removal = -1
                    heappush(level_heights[node_level], (-max_height, node_of_max_height))
            else:
                max_height_after_removal = max_height
                heappush(level_heights[node_level], (-max_height, node_of_max_height))

            result.append(max_height_after_removal + node_level)

        return result
