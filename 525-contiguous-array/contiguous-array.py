class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = -1
        running_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            running_sum += 1 if num == 1 else -1
            if running_sum in prefix_sum:
                max_len = max(max_len, i - prefix_sum[running_sum])
            else:
                prefix_sum[running_sum] = i

        return max_len
                
        