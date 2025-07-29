from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        """
        For each start index i, find the shortest subarray nums[i..j] whose OR equals
        the OR of the entire suffix nums[i..n-1]. We track, for each bit (0–31), the
        closest index ≥ i at which that bit is set, then choose the farthest of these.
        """
        n = len(nums)
        answer = [1] * n
        # For each bit position, store the next index where that bit is 1; -1 if none seen yet
        next_pos = [-1] * 32

        # Traverse from rightmost to leftmost
        for i in range(n - 1, -1, -1):
            x = nums[i]
            # Update next_pos for bits set in nums[i]
            for b in range(32):
                if (x >> b) & 1:
                    next_pos[b] = i

            # Determine how far we must go to include all bits present in the suffix
            farthest = i
            for b in range(32):
                if next_pos[b] != -1:
                    # Extend to the furthest next occurrence among all bits
                    farthest = max(farthest, next_pos[b])

            # Length = (end_index − start_index + 1)
            answer[i] = farthest - i + 1

        return answer
