class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flip_count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                if  i >= (len(nums) - 2):
                    return -1
                else:
                    nums[i] ^= 1
                    nums[i + 1] ^= 1
                    nums[i + 2] ^= 1
                    flip_count += 1
                
        return flip_count

        