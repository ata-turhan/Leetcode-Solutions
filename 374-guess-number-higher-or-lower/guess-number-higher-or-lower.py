# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            num = left + (right-left)//2
            result = guess(num)
            if result == 0:
                return num
            elif result == -1:
                right = num - 1
            elif result == 1:
                left = num + 1
        return -1
        