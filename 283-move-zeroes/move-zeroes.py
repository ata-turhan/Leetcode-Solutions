class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return nums
        z = nums.index(0)
        i = z + 1
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[z] = nums[z], nums[i]
                z += 1
            i += 1


        