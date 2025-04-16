from collections import defaultdict
from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        pairs = 0  # Current count of equal pairs in the window [l, r]
        res = 0    # Result: number of good subarrays
        l = 0
        
        # Expand the window with right pointer r
        for r in range(n):
            # Each new occurrence of nums[r] forms pairs with its previous appearances.
            pairs += freq[nums[r]]
            freq[nums[r]] += 1
            
            # Shrink the window from the left while the subarray has at least k pairs.
            while l <= r and pairs >= k:
                # All subarrays starting at index l and ending from r to n-1 are good.
                res += (n - r)
                
                # Remove nums[l] from the window.
                # It decreases the pair count by (freq[nums[l]] - 1),
                # because it was paired with (freq[nums[l]] - 1) other occurrences.
                pairs -= (freq[nums[l]] - 1)
                freq[nums[l]] -= 1
                l += 1
        
        return res
