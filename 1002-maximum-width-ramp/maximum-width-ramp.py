class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        
        # Step 1: Build a decreasing stack of indices
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)  # Store index of the smaller element
        
        max_width = 0
        
        # Step 2: Iterate from the end of the array to find the maximum ramp width
        for j in range(n - 1, -1, -1):
            # Try to maximize the width by comparing with the stack's top element
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()  # Get the smallest index from the decreasing stack
                max_width = max(max_width, j - i)  # Calculate the width and update max width
        
        return max_width
