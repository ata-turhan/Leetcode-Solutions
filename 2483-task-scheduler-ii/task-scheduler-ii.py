class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        elapsed_time = 0
        earliest_start = defaultdict(int)
        for task in tasks:
            elapsed_time += 1
            if earliest_start[task] > elapsed_time:
                elapsed_time = earliest_start[task] 
            earliest_start[task] = elapsed_time + space + 1
        return elapsed_time
                       