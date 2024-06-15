class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Create a list of tuples with each tuple containing the capital and corresponding profit
        projects = [(c, p) for p, c in zip(profits, capital)]
        
        # Sort the list of projects by capital required
        projects.sort()
        
        # Initialize a max-heap to store the profits of the projects that can be afforded
        max_heap = []
        
        # Initialize the index to keep track of the projects that can be afforded
        i = 0
        
        # Execute k times to find the k most profitable projects
        while k > 0:
            # Push all the projects that can be afforded with the current capital into the max-heap
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            
            # If no more projects can be afforded, break the loop
            if not max_heap:
                break
            
            # Pop the project with the highest profit from the max-heap and add its profit to the current capital
            w += -heapq.heappop(max_heap)
            
            # Decrement k to move to the next iteration
            k -= 1
        
        # Return the maximized capital after k iterations
        return w
