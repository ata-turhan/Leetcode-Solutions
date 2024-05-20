class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by the start time
        intervals.sort(key=lambda x: x[0])
        
        merged_intervals = []

        for interval in intervals:
            # If merged_intervals is empty or there's no overlap, add the interval to the result
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                # There's overlap, merge the intervals
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        
        return merged_intervals
