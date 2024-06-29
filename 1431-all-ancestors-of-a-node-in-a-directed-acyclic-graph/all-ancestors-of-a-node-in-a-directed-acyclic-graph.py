from sortedcontainers import SortedSet

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = [SortedSet() for _ in range(n)]
        queue = deque()
        adj_list = defaultdict(list)
        incoming_edges = [0] * n

        for u, v in edges:
            incoming_edges[v] += 1       
            adj_list[u].append(v) 

        for i in range(n):
            if incoming_edges[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            for neighbour in adj_list[node]:
                ancestors[neighbour].add(node)
                for ancestor in ancestors[node]:
                    ancestors[neighbour].add(ancestor)

                incoming_edges[neighbour] -= 1
                if incoming_edges[neighbour] == 0:
                    queue.append(neighbour)

        return ancestors