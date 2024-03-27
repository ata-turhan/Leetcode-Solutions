class Solution:    
    def connect(self, root: Optional['Node']) -> Optional['Node']:
        def dfs(node):
            if not node:
                return None

            next_node = node.next
            while next_node and next_node.next:
                if next_node.left or next_node.right:
                    break
                else:
                    next_node = next_node.next
                    

            if node.left and node.right:
                node.left.next = node.right
                if next_node:
                    node.right.next = next_node.left or next_node.right
            elif node.left and next_node:
                node.left.next = next_node.left or next_node.right
            elif node.right and next_node:
                node.right.next = next_node.left or next_node.right
            dfs(node.right)
            dfs(node.left)
            return node


        return dfs(root)