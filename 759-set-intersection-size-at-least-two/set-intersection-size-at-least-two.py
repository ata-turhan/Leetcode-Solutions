class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        nums = []
        for start, end in intervals:
            if not nums or nums[-1] < start:
                nums.extend([end - 1, end])
            elif nums[-2] < start:
                nums.append(end)
        return len(nums)