class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                intervals.insert(i, newInterval)
                return intervals
            elif newInterval[0] > intervals[i][1]:
                continue
            else:
                start = min(intervals[i][0], newInterval[0])
                end = max(intervals[i][1], newInterval[1])
                while (i+1) < len(intervals):
                    if end >= intervals[i+1][0]:
                        end = max(end, intervals[i+1][1])
                        intervals.pop(i+1)
                    else:
                        break
                intervals[i][0] = start
                intervals[i][1] = end
                return intervals
        intervals.append(newInterval)
        return intervals

        
