class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ia, ib = 0, 0
        for i in range(len(a)-1, -1, -1):
            ia += int(a[i]) * 2**(len(a)-1-i)
        for i in range(len(b)-1, -1, -1):
            ib += int(b[i]) * 2**(len(b)-1-i)
        if ib > ia:
            ia, ib = ib, ia
        while ib > 0:
            temp = ia ^ ib
            ib = (ia & ib) << 1
            ia = temp
        return bin(ia)[2:]
        
        