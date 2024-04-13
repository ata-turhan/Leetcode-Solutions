class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        # Extract x-coordinates from points
        xs = [point[0] for point in points]
        xs.sort()
        
        # Initialize variables
        i = 0
        res = 0
        
        # Iterate through x-coordinates
        while i < len(xs):
            cur_val = xs[i]
            
            # Find the range of x-coordinates covered by a rectangle
            while i < len(xs) and xs[i] <= cur_val + w:
                i += 1
                
            # Increment the count of rectangles needed
            res += 1
            
        return res
