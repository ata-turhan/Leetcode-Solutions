class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        running_sum = 0
        result = 0

        for num in nums:
            running_sum += num
            if (running_sum - goal) in prefix_sums:
                result += prefix_sums[(running_sum - goal)]
            prefix_sums[running_sum] += 1

        return result
