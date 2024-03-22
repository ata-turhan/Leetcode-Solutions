class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        if zero_count == 0:
            return
            
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        nums[-zero_count:] = [0] * zero_count

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
        """


        