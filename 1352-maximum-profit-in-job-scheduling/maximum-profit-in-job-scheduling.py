from typing import List
import heapq

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Create a sorted list of jobs with (start, end, profit) tuples sorted by start time
        jobs = sorted([(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))])
        
        # Min-heap to keep track of jobs based on their end time
        profit_heap = []
        
        # Track the maximum profit achievable
        current_max_profit = 0
        max_profit = 0
        
        # Process each job in order of start time
        for start, end, job_profit in jobs:
            # Remove jobs from the heap that end before the current job's start time
            while profit_heap and profit_heap[0][0] <= start:
                end_time, profit_up_to = heapq.heappop(profit_heap)
                current_max_profit = max(current_max_profit, profit_up_to)
            
            # Add the current job with its end time and cumulative profit to the heap
            heapq.heappush(profit_heap, (end, current_max_profit + job_profit))
            # Update the max profit if the new job increases it
            max_profit = max(max_profit, current_max_profit + job_profit)
        
        return max_profit
