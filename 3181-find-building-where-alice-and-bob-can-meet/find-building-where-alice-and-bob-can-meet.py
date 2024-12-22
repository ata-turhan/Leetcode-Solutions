class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        
        # 1) Create array of (height, index)
        arr = [(heights[i], i) for i in range(n)]
        # Sort by height ascending, then by index ascending
        arr.sort(key=lambda x: (x[0], x[1]))
        
        # Separate lists for convenience
        heights_sorted = [pair[0] for pair in arr]
        indices_sorted = [pair[1] for pair in arr]
        
        # Helper function to find the leftmost building index > y among those with height > H
        def get_next_building(H, y):
            posH = bisect.bisect_right(heights_sorted, H)
            if posH == n:
                return -1
            
            min_idx = -1
            # **Scan all** valid buildings to find the minimal index
            for i in range(posH, n):
                # We already know that heights_sorted[i] > H
                if indices_sorted[i] > y:
                    if min_idx == -1 or indices_sorted[i] < min_idx:
                        min_idx = indices_sorted[i]
            return min_idx
        
        # Process queries
        ans = []
        for (x, y) in queries:
            # Ensure x <= y
            if x > y:
                x, y = y, x
            
            # Case 1: same building
            if x == y:
                ans.append(x)
                continue
            
            # Case 2: building y is taller => answer is y
            if heights[x] < heights[y]:
                ans.append(y)
                continue
            
            # Case 3: find leftmost building t > y with heights[t] > heights[x]
            t = get_next_building(heights[x], y)
            ans.append(t)
        
        return ans