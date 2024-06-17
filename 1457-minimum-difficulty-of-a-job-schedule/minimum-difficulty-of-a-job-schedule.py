from typing import List
from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], days: int) -> int:
        num_jobs = len(jobDifficulty)
        # If we cannot schedule at least one job per day, it is impossible to create a schedule
        if num_jobs < days:
            return -1
        
        # Precompute the hardest job from the current job to the end
        hardest_job_remaining = [0] * num_jobs
        hardest_job = 0
        for i in range(num_jobs - 1, -1, -1):
            hardest_job = max(hardest_job, jobDifficulty[i])
            hardest_job_remaining[i] = hardest_job
        
        @lru_cache(None)
        def dp(job_index, current_day):
            # Base case: it's the last day, so we need to finish all the jobs
            if current_day == days:
                return hardest_job_remaining[job_index]
            
            min_difficulty = float("inf")
            hardest_in_partition = 0
            # Iterate through the options and choose the best
            for partition_index in range(job_index, num_jobs - (days - current_day)):
                hardest_in_partition = max(hardest_in_partition, jobDifficulty[partition_index])
                min_difficulty = min(min_difficulty, hardest_in_partition + dp(partition_index + 1, current_day + 1))

            return min_difficulty
        
        return dp(0, 1)
