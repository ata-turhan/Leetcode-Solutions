class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # Convert the list to a set for faster lookup
        set_nums = set(nums)
        # Initialize the result variable
        max_k = -1
        # Iterate through each number in the list
        for num in nums:
            # Check if the current number is positive and its negative counterpart exists in the set
            if num > 0 and -num in set_nums:
                # Update the maximum K value
                max_k = max(max_k, num)
        return max_k
