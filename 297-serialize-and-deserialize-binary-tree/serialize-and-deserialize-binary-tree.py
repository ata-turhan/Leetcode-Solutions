# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return "#,"
        
        s = ""
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node is None:
                s += "#,"
            else:
                s += str(node.val) + ","
                queue.append(node.left)
                queue.append(node.right)
        
        return s

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        if not data:
            return None
        
        nodes = data.split(",")
        if nodes[0] == "#":
            return None
        
        nodes.pop()  # Remove the trailing empty string after the last comma
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        i = 1
        
        while queue:
            node = queue.popleft()
            if nodes[i] != "#":
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1
            
            if nodes[i] != "#":
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1
        
        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))