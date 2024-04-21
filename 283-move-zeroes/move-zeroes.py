class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)  # Count the number of zeros in the list
        if zero_count == 0:
            return  # If there are no zeros, no action is needed
        
        k = 0  # Initialize a pointer to keep track of the current position to place non-zero elements
        for i in range(len(nums)):
            if nums[i] != 0:
                # If the current element is non-zero, move it to the position indicated by k
                nums[k] = nums[i]
                k += 1
        # Fill the remaining positions from k to the end of the list with zeros
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


        