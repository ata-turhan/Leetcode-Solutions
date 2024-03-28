# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""

        def serialize_node(node):
            if not node:
                return []

            res = [str(node.val)]
            for child in node.children:
                res.extend(serialize_node(child))
            res.append("#")  # Use "#" to mark the end of children for the current node
            return res

        return " ".join(serialize_node(root))

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        def deserialize_node(nodes):
            if not nodes:
                return None

            val = nodes.pop(0)
            if val == "#":
                return None

            node = Node(int(val))
            node.children = []
            while nodes and nodes[0] != "#":
                node.children.append(deserialize_node(nodes))
            if nodes:
                nodes.pop(0)  # Remove "#" for the current node
            return node

        return deserialize_node(data.split())

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
