# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def encode(self, root: 'Node') -> 'TreeNode':
        """Encodes an N-ary tree to a binary tree.
        
        Args:
            root (Node): The root of the N-ary tree to be encoded.
        
        Returns:
            TreeNode: The root of the corresponding binary tree.
        """
        if not root:
            return None

        # Create a TreeNode for the root of the binary tree
        binary_root = TreeNode(root.val)

        # Encode the first child of the N-ary tree
        if root.children:
            first_child = root.children[0]
            binary_root.left = self.encode(first_child)

        # Encode the rest of the children as the right children of the binary tree
        current = binary_root.left
        for child in root.children[1:]:
            current.right = self.encode(child)
            current = current.right

        return binary_root

    def decode(self, data: 'TreeNode') -> 'Node':
        """Decodes a binary tree to an N-ary tree.
        
        Args:
            data (TreeNode): The root of the binary tree to be decoded.
        
        Returns:
            Node: The root of the corresponding N-ary tree.
        """
        if not data:
            return None

        # Create a Node for the root of the N-ary tree
        nary_root = Node(data.val, [])

        # Decode the children of the binary tree as the children of the N-ary tree
        current = data.left
        while current:
            nary_root.children.append(self.decode(current))
            current = current.right

        return nary_root
