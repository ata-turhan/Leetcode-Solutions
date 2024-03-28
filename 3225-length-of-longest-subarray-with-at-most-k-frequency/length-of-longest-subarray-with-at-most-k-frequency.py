from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # Dictionary to store the frequency of elements in the current window
        element_freq = defaultdict(int)
        
        # Initialize the left pointer, maximum subarray length, and result
        left_ptr = 0
        max_length = 0

        # Iterate over the array using the right pointer
        for right_ptr in range(len(nums)):
            # Update the frequency of the current element
            element_freq[nums[right_ptr]] += 1
            
            # Adjust the window size if any element's frequency exceeds k
            while element_freq[nums[right_ptr]] > k:
                # Decrement the frequency of the leftmost element in the window
                element_freq[nums[left_ptr]] -= 1
                # Move the left pointer to the right
                left_ptr += 1
            
            # Update the maximum subarray length
            max_length = max(max_length, right_ptr - left_ptr + 1)

        return max_length
