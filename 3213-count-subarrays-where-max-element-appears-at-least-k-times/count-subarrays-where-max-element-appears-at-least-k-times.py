from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)  # Find the maximum element in the array
        result = 0  # Initialize the result count
        max_indices = []  # List to store the indices of the maximum element
        
        # Iterate through the array and track the indices of the maximum element
        for i, num in enumerate(nums):
            if num == max_element:
                max_indices.append(i)
            # If the count of maximum element indices reaches or exceeds k
            if len(max_indices) >= k:
                # Increment the result count by the index of the (kth occurrence - k + 1) maximum element
                result += max_indices[-k] + 1
        
        return result
