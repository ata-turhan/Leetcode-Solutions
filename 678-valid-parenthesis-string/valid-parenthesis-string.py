class Solution:
    def checkValidString(self, s: str) -> bool:
        op, star, cl = 0, 0 , 0
        for char in s:
            if char == "(":
                op += 1
            elif char == ")":
                cl += 1
            else:
                star += 1
            if cl > op:
                if star == 0:
                    return False
                else:
                    star -= 1
                    op += 1
        op, star, cl = 0, 0 , 0
        for char in s[::-1]:
            if char == "(":
                op += 1
            elif char == ")":
                cl += 1
            else:
                star += 1
            if op > cl:
                if star == 0:
                    return False
                else:
                    star -= 1
                    cl += 1
        return True
