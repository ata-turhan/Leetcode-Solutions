from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """
        Return the smallest possible maximum difference among p disjoint pairs
        selected from nums. If p == 0, no pairs are chosen and the result is 0.
        """
        # Base case: no pairs ⇒ max difference = 0
        if p == 0:
            return 0

        nums.sort()

        def can_form_pairs(max_diff: int) -> bool:
            """
            Greedily form as many disjoint pairs with difference ≤ max_diff.
            Return True iff we can form at least p pairs.
            """
            count = 0
            i = 0
            n = len(nums)
            while i + 1 < n:
                # If this adjacent pair is within the threshold, take it
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  # skip both elements
                    if count >= p:
                        return True
                else:
                    i += 1  # try next index as start of a pair
            return False

        left, right = 0, nums[-1] - nums[0]
        answer = right

        # Binary search for the minimal feasible max_diff
        while left <= right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
