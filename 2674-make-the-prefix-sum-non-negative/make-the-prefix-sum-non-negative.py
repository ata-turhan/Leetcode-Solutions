class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        min_heap = []
        cumulative_sum = 0
        negative_count = 0

        for num in nums:
            cumulative_sum += num
            heapq.heappush(min_heap, num)
            if cumulative_sum < 0:
                min_num = heapq.heappop(min_heap)
                cumulative_sum -= min_num
                negative_count += 1
        
        return negative_count