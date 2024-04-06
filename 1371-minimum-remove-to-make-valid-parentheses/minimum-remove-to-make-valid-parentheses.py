class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        op, cl = 0, 0
        stack = []
        for char in s:
            stack.append(char)
            if char == "(":
                op += 1
            elif char == ")":
                cl += 1
            if cl > op:
                stack.pop()
                cl -= 1
        if op == cl:
            return "".join(stack)
        else:
            extra_open = op - cl
            res = []
            for i in range(len(stack)-1, -1, -1):
                if stack[i] == "(":
                    extra_open -= 1
                    if extra_open == 0:

                        res.extend(stack[:i][::-1])
                        break
                else:
                    res.append(stack[i])
            return "".join(res[::-1])
                
            
        