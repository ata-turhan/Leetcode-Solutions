import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Finds the k closest points to the origin (0, 0).
        
        :param points: List[List[int]] - A list of points represented as [x, y].
        :param k: int - The number of closest points to find.
        :return: List[List[int]] - A list of the k closest points.
        """
        heap = []  # Initialize a min-heap
        for point in points:
            dist = point[0]**2 + point[1]**2  # Calculate the squared distance from the origin
            heapq.heappush(heap, (dist, point))  # Push the distance and point as a tuple into the heap

        res = []  # List to store the result
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])  # Pop the k smallest elements from the heap and add to the result
        return res  # Return the list of k closest points

# Example usage:
# sol = Solution()
# print(sol.kClosest([[1, 3], [-2, 2]], 1))  # Output: [[-2, 2]]
# print(sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2))  # Output: [[3, 3], [-2, 4]]
