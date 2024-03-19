from heapq import heappush, heappop
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        task_counter = Counter(tasks)
        for task, count in task_counter.items():
            heappush(heap, (0, -count, task))

        time = 0
        while heap:
            min_time, count, task = heappop(heap)
            if min_time > time:
                heappush(heap, (min_time, count, task))
                time = min_time
                continue
            else:
                if count < -1:
                    min_time += n + 1
                    count += 1
                    heappush(heap, (min_time, count, task))
                time += 1
        return time
        