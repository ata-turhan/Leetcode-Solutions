class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        # Get the lengths of both input arrays
        len1, len2 = len(nums1), len(nums2)
        
        # Initialize the DP table with zeros
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        
        # Variable to store the maximum length of repeated subarray
        max_length = 0
        
        # Fill the DP table
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
        
        return max_length