from heapq import heappush, heappop
from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Initialize a heap to store tasks with their counts and start time 0
        heap = []
        # Count the occurrences of each task
        task_counter = Counter(tasks)
        
        # Push tasks onto the heap with a priority based on their counts
        for task, count in task_counter.items():
            # Use negative count to achieve max-heap behavior
            heappush(heap, (0, -count, task))

        # Initialize time
        time = 0
        
        # Process tasks until heap is empty
        while heap:
            # Pop the task with the smallest start time
            min_time, count, task = heappop(heap)
            
            # If the task can't be scheduled yet, push it back with updated start time
            if min_time > time:
                heappush(heap, (min_time, count, task))
                time = min_time
                continue
            else:
                # If the task has remaining occurrences, schedule it and update time
                if count < -1:
                    min_time += n + 1
                    count += 1
                    heappush(heap, (min_time, count, task))
                time += 1
        
        return time
