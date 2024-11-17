class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        shortest_sub_length = len(nums) + 1
        cum_sum = 0
        prev_sums = []
        heappush(prev_sums, (0, -1))

        for i in range(len(nums)):
            cum_sum += nums[i]

            while prev_sums and cum_sum - prev_sums[0][0] >= k:
                _, prev_idx = heappop(prev_sums)
                shortest_sub_length = min(shortest_sub_length, i - prev_idx)

            heappush(prev_sums, (cum_sum, i))

        return shortest_sub_length if shortest_sub_length < len(nums) + 1 else -1
        