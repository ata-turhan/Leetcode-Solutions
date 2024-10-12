class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        starts = [(start, -1) for start, _ in intervals]
        ends = [(end, 1) for _, end in intervals]
        times = starts + ends
        times.sort()
        max_intersection = 0
        running_sum = 0
        for time in times:
            _, value = time
            running_sum += value
            max_intersection = max(max_intersection, abs(running_sum))
        return max_intersection