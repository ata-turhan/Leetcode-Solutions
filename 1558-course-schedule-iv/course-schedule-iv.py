from typing import List
from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Initialize an adjacency list to represent the graph of courses and prerequisites
        course_graph = [set() for _ in range(numCourses)]
        
        # Populate the graph with the given prerequisites
        for course, prereq in prerequisites:
            course_graph[course].add(prereq)

        def bfs(start: int, target: int) -> bool:
            """ Perform BFS to check if there is a path from start course to target course """
            queue = deque([start])  # Queue for BFS initialized with the start node
            visited = set([start])  # Set to keep track of visited nodes

            while queue:
                current_course = queue.popleft()  # Dequeue the next course to process
                if current_course == target:  # If we reach the target course, return True
                    return True
                # Traverse the neighbors (prerequisites) of the current course
                for neighbor in course_graph[current_course]:
                    if neighbor not in visited:  # If the neighbor hasn't been visited
                        queue.append(neighbor)  # Add it to the queue for processing
                        visited.add(neighbor)  # Mark it as visited
            return False  # Return False if no path from start to target is found

        result = []
        # Process each query to determine if one course is a prerequisite for another
        for start_course, target_course in queries:
            result.append(bfs(start_course, target_course))  # Append the result of BFS for each query

        return result  # Return the list of results for all queries
