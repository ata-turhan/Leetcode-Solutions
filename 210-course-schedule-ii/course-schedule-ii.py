from collections import deque, defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Initialize the result list that will store the course order
        course_order = []
        # Initialize a queue to process courses with no prerequisites
        course_queue = deque()
        # Initialize adjacency list to represent the graph
        adjacency_list = defaultdict(list)
        # Initialize in-degree count for each course
        course_in_degree = defaultdict(int)

        # Build the graph and count in-degrees
        for course, prereq in prerequisites:
            course_in_degree[course] += 1
            adjacency_list[prereq].append(course)

        # Add courses with no prerequisites to the queue
        for course in range(numCourses):
            if course_in_degree[course] == 0:
                course_queue.append(course)

        # Process the courses in topological order
        while course_queue:
            current_course = course_queue.popleft()
            course_order.append(current_course)

            # Decrease in-degree of neighboring courses
            for neighbor in adjacency_list[current_course]:
                course_in_degree[neighbor] -= 1
                # If in-degree becomes zero, add to the queue
                if course_in_degree[neighbor] == 0:
                    course_queue.append(neighbor)

        # If we processed all courses, return the order; otherwise, return an empty list
        return course_order if len(course_order) == numCourses else []
