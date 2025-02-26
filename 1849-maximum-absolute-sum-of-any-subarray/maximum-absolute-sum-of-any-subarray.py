class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Initialize running sums and global max/min
        max_sum = cur_max = 0
        min_sum = cur_min = 0
        
        # Process each element in the array
        for x in nums:
            # Update the running maximum subarray sum
            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum, cur_max)
            
            # Update the running minimum subarray sum
            cur_min = min(x, cur_min + x)
            min_sum = min(min_sum, cur_min)
        
        # The result is the maximum between the max subarray sum and the absolute value of the min subarray sum
        return max(max_sum, -min_sum)

        