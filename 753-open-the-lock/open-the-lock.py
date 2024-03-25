class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" == target:
            return 0

        q = deque()
        if "0000" not in deadends:
            q.append(("0000", 0))
        
        visited = set()
        visited.add("0000")

        while q:
            node, dist = q.popleft()

            for i in range(4):
                new_node1 = node[:i] + str((int(node[i]) + 1) % 10) + node[i+1:]
                new_node2 =  node[:i] + str((int(node[i]) - 1) % 10) + node[i+1:]

                if new_node1 == target or new_node2 == target:
                    return dist + 1
                if new_node1 not in deadends and new_node1 not in visited:
                    visited.add(new_node1)
                    q.append((new_node1, dist + 1))
                if new_node2 not in deadends and new_node2 not in visited:
                    visited.add(new_node2)
                    q.append((new_node2, dist + 1))
        return -1