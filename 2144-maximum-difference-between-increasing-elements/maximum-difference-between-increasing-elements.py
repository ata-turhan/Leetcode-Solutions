class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_dif = -1
        max_so_far = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < max_so_far:
                max_dif = max(max_dif, max_so_far - nums[i])
            max_so_far = max(max_so_far, nums[i])
            
        return max_dif
        