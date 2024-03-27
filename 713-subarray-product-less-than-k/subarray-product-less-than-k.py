class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        
        prod = 1  # Initialize product of elements in the current subarray
        ans = 0   # Initialize the count of subarrays with product less than k
        left = 0  # Initialize the left pointer
        
        # Iterate through the elements in the list
        for right, val in enumerate(nums):
            prod *= val  # Update the product by multiplying with the current element
            
            # Shrink the window by moving the left pointer until the product is less than k
            while prod >= k:
                prod /= nums[left]
                left += 1
            
            # Count the subarrays ending at the current position
            ans += right - left + 1
        
        return ans  # Return the total count of subarrays with product less than k
