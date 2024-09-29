class ListNode:
    def __init__(self, count: int):
        # Each node stores a count and a set of keys with that count
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        # Maps each key to its count
        self.key_count = {}
        # Maps each count to the corresponding ListNode
        self.count_map = {}
        # Sentinel head (for minimum count) and tail (for maximum count)
        self.head = ListNode(float('-inf'))
        self.tail = ListNode(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert_after(self, new_node: ListNode, prev_node: ListNode):
        # Insert new_node after prev_node in the linked list
        next_node = prev_node.next
        new_node.prev = prev_node
        new_node.next = next_node
        prev_node.next = new_node
        next_node.prev = new_node

    def _remove_node(self, node: ListNode):
        # Remove node from the linked list if it's empty
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del self.count_map[node.count]

    def inc(self, key: str) -> None:
        if key in self.key_count:
            self._change_count(key, 1)  # Increment the existing key's count
        else:
            # New key, initialize with count 1
            self.key_count[key] = 1
            if 1 not in self.count_map:
                new_node = ListNode(1)
                self.count_map[1] = new_node
                self._insert_after(new_node, self.head)  # Insert at the beginning
            self.count_map[1].keys.add(key)

    def dec(self, key: str) -> None:
        if key in self.key_count:
            self._change_count(key, -1)  # Decrement the existing key's count

    def _change_count(self, key: str, delta: int):
        # Update the count of key and move it between nodes accordingly
        count = self.key_count[key]
        new_count = count + delta
        current_node = self.count_map[count]

        if new_count == 0:
            # If count drops to 0, remove the key completely
            del self.key_count[key]
        else:
            self.key_count[key] = new_count
            if new_count not in self.count_map:
                # Create a new node for the new count
                new_node = ListNode(new_count)
                self.count_map[new_count] = new_node
                # Insert the new node in the correct position
                if delta == 1:
                    self._insert_after(new_node, current_node)  # Higher count goes after
                else:
                    self._insert_after(new_node, current_node.prev)  # Lower count goes before
            self.count_map[new_count].keys.add(key)

        # Remove the key from the current node's keys set
        current_node.keys.remove(key)
        # If the current node has no keys left, remove it
        if not current_node.keys:
            self._remove_node(current_node)

    def getMaxKey(self) -> str:
        # Return any key from the node with the highest count (tail's previous node)
        if self.tail.prev == self.head:
            return ""  # No keys exist
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        # Return any key from the node with the lowest count (head's next node)
        if self.head.next == self.tail:
            return ""  # No keys exist
        return next(iter(self.head.next.keys))
