class Solution:
    def countAndSay(self, n: int) -> str:
        num = ["1"]
        for i in range(n-1):
            count = 1
            prev = num[0]
            new_num = []
            for j in range(1, len(num)):
                if num[j] == prev:
                    count += 1
                else:
                    new_num.extend(list(str(count)))
                    new_num.append(prev)
                    count = 1
                    prev = num[j]
            new_num.extend(list(str(count)))
            new_num.append(prev)
            num = new_num
            print(num)
        return "".join(map(str, num))
        