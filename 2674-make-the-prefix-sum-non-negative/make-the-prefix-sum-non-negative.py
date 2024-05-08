class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        heap = []
        cumsum = 0
        count = 0

        for num in nums:
            cumsum += num
            heapq.heappush(heap, num)
            if cumsum < 0:
                min_num = heapq.heappop(heap)
                cumsum -= min_num
                count += 1
        return count