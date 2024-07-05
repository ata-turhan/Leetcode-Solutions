class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the area formed by the two lines
            current_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current_area)
            
            # Move the pointer of the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
