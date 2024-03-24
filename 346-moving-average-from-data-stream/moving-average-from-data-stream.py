class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.sum_ = 0
        self.len = 0
        self.size = size
        

    def next(self, val: int) -> float:
        self.sum_ += val
        self.q.append(val)
        if self.len == self.size:
            removed_val = self.q.popleft()
            self.sum_ -= removed_val
        else:
            self.len += 1
        return self.sum_ / self.len


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)