from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        Return the number of subarrays filled with 0.

        Idea:
        - Maintain `consecutive` = number of consecutive zeros ending at current index.
        - When nums[i] == 0, increment `consecutive` and add it to the total answer.
          (Because every new zero extends all previous zero-only subarrays ending before it
           and also forms the subarray consisting of itself.)
        - When nums[i] != 0, reset `consecutive` to 0.

        Complexity: O(n) time, O(1) extra space.
        """
        total = 0          # total zero-filled subarrays
        consecutive = 0    # consecutive zeros ending at current position

        for x in nums:
            if x == 0:
                consecutive += 1
                total += consecutive
            else:
                consecutive = 0

        return total
