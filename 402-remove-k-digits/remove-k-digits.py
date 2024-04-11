class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        # Iterate through each digit in num
        for digit in num:
            # Remove digits from the stack while the current digit is smaller than the top element and k > 0
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If k > 0, remove remaining digits from the stack
        while k > 0:
            stack.pop()
            k -= 1
        
        # Construct the resulting string while ignoring leading zeros
        result = ''.join(stack).lstrip('0')
        return result if result else '0'  # If result is empty, return '0'
