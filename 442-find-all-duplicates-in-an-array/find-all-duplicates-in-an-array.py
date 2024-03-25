class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            # Get the absolute value of the current number
            abs_num = abs(num)
            # Check if the element at the index of the absolute value minus 1 is negative
            # If it is, it means this element has been encountered before, so it's a duplicate
            if nums[abs_num - 1] < 0:
                res.append(abs_num)
            else:
                # Mark the element at the index of the absolute value minus 1 as negative
                nums[abs_num - 1] *= -1
        return res
