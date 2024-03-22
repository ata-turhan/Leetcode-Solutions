from itertools import chain

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        res = [[] for _ in range(m+n-1)]
        
        for i, row in enumerate(mat):
            for j, num in enumerate(row):
                res[i+j].append(num)
        
        reverse = True
        for i in range(len(res)):
            if reverse:
                res[i] = res[i][::-1]
            reverse = not reverse
        
        return list(chain.from_iterable(res))
        