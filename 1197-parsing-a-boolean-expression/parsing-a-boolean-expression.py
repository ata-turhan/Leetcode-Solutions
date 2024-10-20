from functools import reduce

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        # Iterate through each character in the expression
        for char in expression:
            if char == ",":
                continue  # Skip commas
            elif char == ")":
                # Build the subexpression between the parentheses
                sub_expression = []
                while stack[-1] != "(":
                    sub_expression.append(stack.pop())
                stack.pop()  # Pop the opening '('
                operator = stack.pop()  # Pop the operator ('!', '&', '|')

                # Evaluate the subexpression based on the operator
                if operator == "!":
                    evaluated_value = "f" if sub_expression[0] == "t" else "t"
                elif operator == "&":
                    evaluated_value = "t" if all(val == "t" for val in sub_expression) else "f"
                elif operator == "|":
                    evaluated_value = "t" if any(val == "t" for val in sub_expression) else "f"
                
                # Append the evaluated value back to the stack
                stack.append(evaluated_value)
            else:
                # Add character (either 't', 'f', '(', '!', '&', '|') to the stack
                stack.append(char)

        # Return the final result as boolean (True for 't', False for 'f')
        return stack[0] == "t"
