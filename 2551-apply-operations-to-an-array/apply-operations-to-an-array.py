class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            if nums[i] != 0:
                res.append(nums[i])

        if nums[-1] != 0:
            res.append(nums[-1])

        res.extend([0] * (len(nums) - len(res)))

        return res

        
        