# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []  # Initialize children as an empty list if not provided

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""

        # Helper function to serialize a node and its children
        def serialize_node(node):
            if not node:
                return []

            res = [str(node.val)]  # Convert the node value to string and add to result list
            for child in node.children:
                res.extend(serialize_node(child))  # Serialize each child recursively
            res.append("#")  # Use "#" to mark the end of children for the current node
            return res

        return " ".join(serialize_node(root))  # Join the serialized nodes with space

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        nodes = data.split()  # Split the serialized string into tokens

        # Helper function to deserialize nodes from the token list
        def deserialize_node(nodes):
            if not nodes:
                return None

            val = nodes.pop(0)  # Pop the first token as the node value
            if val == "#":
                return None  # Return None if "#" is encountered, indicating the end of children

            node = Node(int(val))  # Convert the token to integer and create a new node
            node.children = []
            while nodes and nodes[0] != "#":
                node.children.append(deserialize_node(nodes))  # Deserialize children recursively
            if nodes:
                nodes.pop(0)  # Remove "#" for the current node
            return node

        return deserialize_node(nodes)
