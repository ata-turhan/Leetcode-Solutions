from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        Return the count of non-empty subsequences whose minimum + maximum <= target.
        Uses sorting + two pointers + precomputed powers of two modulo 1e9+7.
        """
        MOD: int = 10**9 + 7
        n: int = len(nums)
        
        # 1. Sort the array
        nums.sort()
        
        # 2. Precompute powers of two: pow2[k] = 2^k % MOD
        pow2: List[int] = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        result: int = 0
        left: int = 0
        right: int = n - 1
        
        # 3. Two-pointer traversal
        while left <= right:
            # If the smallest (nums[left]) + largest (nums[right]) <= target,
            # then all subsets of elements in between also satisfy the condition.
            if nums[left] + nums[right] <= target:
                result = (result + pow2[right - left]) % MOD
                left += 1  # move to next potential minimum
            else:
                # too large, need to decrease the maximum
                right -= 1
        
        return result
