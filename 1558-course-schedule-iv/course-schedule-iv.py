class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [set() for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].add(v)

        def bfs(u, v, visited):
            q = deque()
            q.append(u)
            visited.add(u)
            while q:
                node = q.popleft()
                if node == v:
                    return True
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        q.append(neighbour)
                        visited.add(neighbour)
            return False

        res = []
        for u, v in queries:
            if bfs(u, v, set()):
                res.append(True)
            else:
                res.append(False)

        return res
                