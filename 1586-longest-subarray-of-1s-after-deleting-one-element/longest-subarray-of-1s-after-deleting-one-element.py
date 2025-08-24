class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Sliding window with at most one zero inside it.
        left = 0
        zeros = 0
        best = 0

        for right, x in enumerate(nums):
            if x == 0:
                zeros += 1

            # If we have more than one zero, shrink from the left
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # Window length is (right - left + 1); we must delete one element.
            # If the window has a zero, we delete that zero; otherwise we delete a 1.
            best = max(best, right - left)  # equals (right - left + 1) - 1

        return best
