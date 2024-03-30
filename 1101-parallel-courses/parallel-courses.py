from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        min_semesters = 0  # Initialize the minimum semesters required
        courses = []  # List to store the order of courses

        # Create an adjacency list and calculate in-degree for each course
        adj_list = defaultdict(list)
        in_degree = [0] * (n + 1)
        for prev, next_ in relations:
            adj_list[prev].append(next_)
            in_degree[next_] += 1

        # Initialize a queue with courses having no prerequisites
        queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])

        # Perform topological sorting using BFS
        while queue:
            size = len(queue)
            for _ in range(size):
                course = queue.popleft()  # Take a course from the queue
                courses.append(course)  # Add the course to the order
                for neighbour in adj_list[course]:
                    in_degree[neighbour] -= 1  # Decrement in-degree of neighbours
                    if in_degree[neighbour] == 0:
                        queue.append(neighbour)  # Add neighbour to the queue if in-degree becomes 0
            min_semesters += 1  # Increment the semester count

        # Return the minimum semesters if all courses are taken, otherwise return -1
        return min_semesters if len(courses) == n else -1
