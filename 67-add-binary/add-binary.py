class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            prefix = "0" * (len(a)-len(b))
            b = prefix + b
        elif len(b) > len(a):
            prefix = "0" * (len(b)-len(a))
            a = prefix + a
        
        res = [0] * len(a)
        carry = 0
        for i in range(len(a)-1, -1, -1):
            sum_ = int(a[i]) + int(b[i]) + carry
            if sum_ < 2:
                carry = 0
                res[i] = str(sum_)
            else:
                carry = 1
                res[i] = str(sum_ % 2)
        if carry:
            res.insert(0, "1")
        return "".join(res)



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
        
        