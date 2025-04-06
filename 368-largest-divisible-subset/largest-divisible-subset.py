class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        dp = [1] * n  # Each element is at least a subset of size 1 (itself)
        prev = [-1] * n  # To reconstruct the subset
        max_index = 0  # Index of the largest subset's last element
        
        # Build up the dp table
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > dp[max_index]:
                max_index = i
        
        # Reconstruct the largest divisible subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]
        
        return result[::-1]  # Reverse to get the subset in increasing order
