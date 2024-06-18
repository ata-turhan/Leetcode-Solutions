class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Create a list of tuples containing negative profit and its index
        profit_indices = [(-p, i) for i, p in enumerate(profit)]
        
        # Convert the list into a heap (min-heap based on negative profit)
        heapify(profit_indices)
        
        # Sort the worker list to assign them to the most profitable job they can do
        worker.sort()
        worker_index = len(worker) - 1
        total_profit = 0
        
        # Get the maximum profit and its corresponding index
        max_profit, max_profit_index = heappop(profit_indices)
        max_profit = -max_profit
        
        # Iterate over workers in reverse order (from highest to lowest capability)
        while worker_index >= 0:
            # Check if the current worker can perform the job with the maximum profit
            if worker[worker_index] >= difficulty[max_profit_index]:
                total_profit += max_profit
                worker_index -= 1
            else:
                # If not, get the next highest profit job
                if profit_indices:
                    max_profit, max_profit_index = heappop(profit_indices)
                    max_profit = -max_profit
                else:
                    break
        
        return total_profit
