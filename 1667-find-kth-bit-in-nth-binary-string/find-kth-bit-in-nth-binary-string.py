class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def findNthNum(n):
            if n == 1:
                return "0"
            s = [0]
            for _ in range(1, n):
                s = s + [1] + list(reversed([1-num for num in s]))
            return "".join(map(str, s))
            
        num = findNthNum(n)
        print(num)
        return num[k-1]
        