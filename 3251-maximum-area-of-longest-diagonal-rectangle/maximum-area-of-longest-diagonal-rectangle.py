class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        longest_diagonal = 0
        largest_area = 0

        for dimension in dimensions:
            a, b = dimension
            if a*a + b*b == longest_diagonal:
                largest_area = max(largest_area, a*b)
            elif a*a + b*b > longest_diagonal:
                longest_diagonal = a*a + b*b
                largest_area = a*b

        return largest_area
        