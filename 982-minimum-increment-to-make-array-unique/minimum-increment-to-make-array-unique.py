class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        running_max = nums[0]
        inc_count = 0

        for num in nums[1:]:
            if num <= running_max:
                inc_count += running_max - num + 1
                num = running_max + 1
            running_max = num

        return inc_count
        