class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        # If the height list has only one element, no trapping is possible, return 0
        if len(height) == 1:
            return 0
        
        stack = [height[0]]  # Initialize a stack with the first element of height list
        for num in height[1:]:
            if stack[0] > num:
                stack.append(num)
            else:
                arr = []
                while len(stack) > 1:
                    arr.append(stack.pop())
                # Calculate the trapped water between the current element and the previous element in the stack
                count = stack[0] * len(arr) - sum(arr)
                res += count
                stack.pop()
                stack.append(num)

        # Reset stack for iterating in reverse order
        stack = [height[-1]]
        for num in height[::-1][1:]:
            if stack[0] >= num:
                stack.append(num)
            else:
                arr = []
                while len(stack) > 1:
                    arr.append(stack.pop())
                # Calculate the trapped water between the current element and the previous element in the stack
                count = stack[0] * len(arr) - sum(arr)
                res += count
                stack.pop()
                stack.append(num)
        return res
