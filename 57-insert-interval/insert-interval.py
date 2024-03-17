class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            i += 1
            
        res.append(newInterval)
        return res
        
        """
        merged = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        merged.append(newInterval)
        merged.extend(intervals[i:])
        return merged
        """
                    

        
