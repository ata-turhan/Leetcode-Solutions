class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        # Initialize variables
        left_index = 0
        total_subarrays = 0
        
        # Iterate through the array
        for right_index in range(len(nums)):
            # If current element is equal to previous element, update left index
            if right_index != 0 and nums[right_index] == nums[right_index - 1]:
                left_index = right_index
            
            # Add the count of subarrays from left to right to the total count
            total_subarrays += right_index - left_index + 1
        
        return total_subarrays
