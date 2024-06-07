class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        res = []
        is_negative = num < 0
        num = abs(num)

        while num > 0:
            remainder = num % 7
            res.append(remainder)
            num //= 7

        base7num = "".join(map(str, res[::-1]))
        
        if is_negative:
            base7num = "-" + base7num

        return base7num
        