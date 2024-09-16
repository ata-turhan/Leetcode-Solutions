class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for timePoint in timePoints:
            minute = int(timePoint[:2]) * 60 + int(timePoint[3:])
            minutes.append(minute)

        minutes.sort()
        min_diff = float("inf")
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])

        min_diff = min(min_diff, 24*60 - (minutes[-1] - minutes[0]))

        return min_diff
        