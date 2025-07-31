from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        """
        Returns the number of distinct bitwise-OR results of all non-empty subarrays of arr.
        """
        # all_ors will hold every distinct OR-value seen so far
        all_ors = set()
        # prev_ors holds OR-values of subarrays ending at the previous element
        prev_ors = set()
        
        for a in arr:
            # Start new OR set for subarrays ending at current element
            # Always include the subarray [a] itself
            curr_ors = {a}
            
            # Extend previous subarrays by OR-ing with current element a
            for prev in prev_ors:
                curr_ors.add(prev | a)
            
            # Merge into global set
            all_ors |= curr_ors
            
            # Update prev_ors for next iteration
            prev_ors = curr_ors
        
        # The number of distinct OR results is the size of all_ors
        return len(all_ors)
