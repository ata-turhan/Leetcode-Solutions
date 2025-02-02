class Solution:
    def check(self, nums: List[int]) -> bool:
        count_breaks = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Check breakpoints (consider circular array)
                count_breaks += 1
                if count_breaks > 1:  # More than one break → not a rotated sorted array
                    return False

        return True
