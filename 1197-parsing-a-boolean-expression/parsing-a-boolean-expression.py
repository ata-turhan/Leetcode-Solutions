class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        i = 0
        
        for i in range(len(expression)):
            if expression[i] == ",":
                pass
            elif expression[i] == ")":
                sub_exp = []
                while stack[-1] != "(":
                    sub_exp.append(stack.pop())
                stack.pop()
                operator = stack.pop()
                if operator == "!":
                    new_val = "f" if sub_exp[0] == "t" else "t"
                elif operator == "&":
                    new_val = reduce(lambda a, b: a and b, [ True if val == "t" else False for val in sub_exp])
                    new_val = "t" if new_val else "f"
                elif operator == "|":
                    new_val = reduce(lambda a, b: a or b, [ True if val == "t" else False for val in sub_exp])
                    new_val = "t" if new_val else "f"
                stack.append(new_val)
            else:
                stack.append(expression[i])
                

        return True if stack[0] == "t" else False