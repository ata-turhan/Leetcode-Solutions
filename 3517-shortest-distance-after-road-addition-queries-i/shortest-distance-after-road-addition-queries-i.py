class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in range(n-1):
            graph[i].append(i+1)

        def bfs(graph):
            queue = deque([(0, 0)])
            visited = set()

            while queue:
                cur_node, cur_step = queue.popleft()
                visited.add(cur_node)

                if cur_node == n - 1:
                    return cur_step

                for neighbor in graph[cur_node]:
                    if neighbor in visited:
                        continue
                    queue.append((neighbor, cur_step + 1))

            return -1

        res = []

        for source, destination in queries:
            graph[source].append(destination)
            steps = bfs(graph)
            res.append(steps)

        return res
        