class Solution:
    def countPrimes(self, n: int) -> int:
        arr = [True] * (n)
        arr[0:2] = [False] * 2
        for i in range(2, int(n**0.5)+1):
            for j in range(i+i, n, i):
                arr[j] = False
        return sum(arr)
        