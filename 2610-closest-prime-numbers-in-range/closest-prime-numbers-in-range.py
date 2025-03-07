class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True] * (1 + right)
        prime[1] = False
        for i in range(2, right + 1):
            if prime[i] == True:
                for j in range(i * i, right + 1, i):
                    prime[j] = False

        
        num1, num2 = -1, -1

        for i in range(left, right + 1):
            if prime[i] == True:
                num1 = i   
                break     

        if num1 == -1:
            return [-1, -1]

        for i in range(num1 + 1, right+1):
            if prime[i] == True:
                num2 = i
                break

        if num2 == -1:
            return [-1, -1]

        min_diff = num2 - num1
        res = [num1, num2]

        prime_second = num2
        for i in range(prime_second + 1, right+1):
            if prime[i] == True:
                num1 = num2
                num2 = i
                if  (num2 - num1) < min_diff:
                    min_diff = num2 - num1
                    res = [num1, num2]

        print(min_diff)

        return res




        