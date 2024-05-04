class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # Initialize the result list
        res = []

        # If the input list is empty, return a single range from lower to upper
        if not nums:
            return [[lower, upper]]

        # Check for missing ranges at the beginning
        if nums[0] != lower:
            res.append([lower, nums[0]-1])

        # Check for missing ranges between consecutive elements
        for i in range(len(nums)-1):
            if nums[i]+1 != nums[i+1]:
                res.append([nums[i]+1, nums[i+1]-1])

        # Check for missing ranges at the end
        if nums[-1] != upper:
            res.append([nums[-1]+1, upper])
        
        return res
