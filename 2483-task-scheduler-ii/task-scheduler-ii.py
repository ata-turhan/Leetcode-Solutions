from collections import defaultdict

class Solution:
    def taskSchedulerII(self, tasks: List[int], cooldown: int) -> int:
        current_day = 0
        next_available_day = defaultdict(int)

        for task in tasks:
            current_day += 1
            # If the task can't be scheduled yet, wait until the next available day
            if next_available_day[task] > current_day:
                current_day = next_available_day[task]
            # Schedule the task and update when it can next be executed
            next_available_day[task] = current_day + cooldown + 1

        return current_day
