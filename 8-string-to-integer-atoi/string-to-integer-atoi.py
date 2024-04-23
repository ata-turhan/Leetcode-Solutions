class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':  # skipping space characters at the beginning
            i+= 1

        positive = 0
        negative = 0

        if i<n and s[i] == '+':
            positive += 1  # number of positive signs at the start in string
            i+= 1

        if i<n and s[i] == '-':
            negative += 1  # number of negative signs at the start in string
            i+= 1

        ans = 0.0

        while i < n and '0' <= s[i] <= '9':
            ans = ans * 10 + (ord(s[i]) - ord('0'))  # converting character to integer
            i+= 1

        if negative > 0:  # if negative sign exists
            ans = -ans

        if positive > 0 and negative > 0:  # if both +ve and -ve signs exist, Example: +-12
            return 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if ans > INT_MAX:  # if ans > 2^31 - 1
            ans = INT_MAX

        if ans < INT_MIN:  # if ans < -2^31
            ans = INT_MIN

        return int(ans)