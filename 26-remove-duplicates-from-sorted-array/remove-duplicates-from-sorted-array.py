class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0  # Initialize pointer k
        # Iterate through the list
        for i in range(1, len(nums)):
            # If current number is different from previous number, update nums[k+1] and increment k
            if nums[k] != nums[i]:
                nums[k + 1] = nums[i]
                k += 1
        return k + 1  # Return the length of the modified list
