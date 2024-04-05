class Solution:
    def makeGood(self, s: str) -> str:
        stack = []  # Initialize a stack to store characters
        for char in s:
            if not stack:  # If the stack is empty, append the current character
                stack.append(char)
            else:
                # Check if the current character and the top of the stack form a pair
                if stack[-1].lower() != char.lower() or stack[-1] == char:
                    stack.append(char)  # If not, append the current character to the stack
                else:
                    stack.pop()  # If they form a pair, pop the character from the stack
        return "".join(stack)  # Convert the stack to a string and return
