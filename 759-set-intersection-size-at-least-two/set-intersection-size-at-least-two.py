class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 2
        
        containing_set = []
        intervals.sort(key=lambda x: (x[1], -x[0]))
        containing_set.append(intervals[0][1] - 1)
        containing_set.append(intervals[0][1])

        for interval in intervals[1:]:
            if containing_set[-1] < interval[0]:
                containing_set.append(interval[1] - 1)
                containing_set.append(interval[1])
            elif containing_set[-2] < interval[0]:
                containing_set.append(interval[1])

        return len(containing_set)
        