from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        """
        Finds the rectangle with the longest diagonal.
        If multiple rectangles have the same diagonal length,
        the one with the largest area is chosen.
        """
        max_diagonal_sq = 0
        max_area = 0

        for width, height in dimensions:
            diagonal_sq = width ** 2 + height ** 2
            area = width * height

            if diagonal_sq > max_diagonal_sq:
                max_diagonal_sq = diagonal_sq
                max_area = area
            elif diagonal_sq == max_diagonal_sq:
                max_area = max(max_area, area)

        return max_area
