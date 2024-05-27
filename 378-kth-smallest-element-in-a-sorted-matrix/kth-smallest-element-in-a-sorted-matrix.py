from heapq import heappush, heappop
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Finds the k-th smallest element in a sorted matrix.
        
        :param matrix: List[List[int]] - A 2D list of integers where each row and column is sorted.
        :param k: int - The rank of the smallest element to find.
        :return: int - The k-th smallest element in the matrix.
        """
        m, n = len(matrix), len(matrix[0])  # Number of rows and columns in the matrix
        
        # Initialize a min-heap
        minHeap = []
        
        # Push the first element of each row into the min-heap
        for r in range(min(k, m)):
            heappush(minHeap, (matrix[r][0], r, 0))
        
        ans = -1  # Initialize answer with a dummy value
        
        # Extract-min k times from the min-heap
        for i in range(k):
            ans, r, c = heappop(minHeap)
            # If there are more elements in the same row, push the next element into the heap
            if c + 1 < n:
                heappush(minHeap, (matrix[r][c + 1], r, c + 1))
        
        return ans

# Example usage:
# sol = Solution()
# print(sol.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))  # Output: 13
