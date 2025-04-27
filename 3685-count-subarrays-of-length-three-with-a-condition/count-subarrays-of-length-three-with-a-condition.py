class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        subarray_count = 0

        for i in range(len(nums)-2):
            if (nums[i] + nums[i + 2]) == nums[i + 1] / 2:
                subarray_count += 1

        return subarray_count
        