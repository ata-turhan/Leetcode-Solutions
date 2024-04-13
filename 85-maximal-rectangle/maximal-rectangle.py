class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols + 1)
        max_area = 0
        
        for row in matrix:
            for col in range(cols):
                # Update the height if the current element is '1', else reset to 0
                heights[col] = heights[col] + 1 if row[col] == '1' else 0
            
            # Calculate the maximum area of a rectangle using the updated histogram heights
            stack = [-1]  # Initialize stack with a sentinel value
            for i in range(cols + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - 1 - stack[-1]
                    max_area = max(max_area, h * w)
                stack.append(i)
        
        return max_area
