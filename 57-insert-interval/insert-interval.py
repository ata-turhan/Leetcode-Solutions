class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        while i < len(intervals):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        return res

                    

        
