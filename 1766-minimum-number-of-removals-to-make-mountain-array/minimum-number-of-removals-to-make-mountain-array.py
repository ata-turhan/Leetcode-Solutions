class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Compute the Longest Increasing Subsequence (LIS) ending at each index
        LIS = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        
        # Compute the Longest Decreasing Subsequence (LDS) starting from each index
        LDS = [1] * n
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    LDS[i] = max(LDS[i], LDS[j] + 1)
        
        # Find the maximum mountain array length
        max_mountain_len = 0
        for i in range(1, n - 1):
            if LIS[i] >= 2 and LDS[i] >= 2:
                max_mountain_len = max(max_mountain_len, LIS[i] + LDS[i] - 1)
        
        # Minimum removals is total length minus the maximum mountain length
        return n - max_mountain_len
