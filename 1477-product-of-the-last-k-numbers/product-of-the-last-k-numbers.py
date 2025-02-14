class ProductOfNumbers:

    def __init__(self):
        self.stream = []
        self.max_zero_index = -1
        self.prefix = []
        

    def add(self, num: int) -> None:
        self.stream.append(num)
        if num == 0:
            self.max_zero_index = len(self.stream) - 1
            self.prefix.append(1)
        else:
            if self.prefix:
                self.prefix.append(self.prefix[-1] * num)
            else:
                self.prefix.append(num)

        

    def getProduct(self, k: int) -> int:
        start_idx = len(self.stream) - k
        if start_idx <= self.max_zero_index:
            return 0
        else:
            if start_idx == 0:
                return self.prefix[-1]
            else:
                return int(self.prefix[-1] / self.prefix[start_idx - 1])
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)