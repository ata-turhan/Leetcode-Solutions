from typing import List
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        Finds the k weakest rows in the matrix mat. The weakness of a row is defined by the number of soldiers (1s)
        present in the row. In case of ties, the row with the smaller index is considered weaker.
        
        :param mat: List[List[int]] - A list of lists representing the matrix.
        :param k: int - The number of weakest rows to find.
        :return: List[int] - The list of indices of the k weakest rows.
        """
        def binarySearch(arr: List[int]) -> int:
            """
            Performs binary search to find the number of soldiers (1s) in the row.
            
            :param arr: List[int] - The row of the matrix.
            :return: int - The count of soldiers in the row.
            """
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == 1:
                    left = mid + 1
                else:
                    right = mid - 1
            return left  # Number of 1s in the row
        
        # Create a priority queue (min-heap) with (number of soldiers, row index)
        queue = [(binarySearch(row), idx) for idx, row in enumerate(mat)]
        heapq.heapify(queue)  # Transform the list into a heap
        
        # Extract the indices of the k weakest rows
        return [idx for _, idx in heapq.nsmallest(k, queue)]

# Example usage:
# sol = Solution()
# print(sol.kWeakestRows([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 1, 0, 0], [1, 1, 1, 1, 1]], 3))  # Output: [2, 0, 3]
