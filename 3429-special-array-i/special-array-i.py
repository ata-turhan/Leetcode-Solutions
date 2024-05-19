class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True  # A single-element array is always special

        is_even = nums[0] % 2 == 0  # Determine if the first number is even or odd

        for i in range(1, len(nums)):
            if is_even and nums[i] % 2 == 0:
                return False  # Two consecutive even numbers
            elif not is_even and nums[i] % 2 != 0:
                return False  # Two consecutive odd numbers
            is_even = not is_even  # Toggle is_even for next iteration

        return True  # All checks passed, array is special
