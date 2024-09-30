class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        # To store incremental values lazily
        self.increment_arr = [0] * maxSize
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        

    def pop(self) -> int:
        if not self.stack:
            return -1
        index = len(self.stack) - 1
        # Apply any lazy increments
        if index > 0:
            self.increment_arr[index - 1] += self.increment_arr[index]
        res = self.stack.pop() + self.increment_arr[index]
        self.increment_arr[index] = 0  # Reset the increment for this index
        return res
        

    def increment(self, k: int, val: int) -> None:
        # Apply the increment lazily for the first k elements
        i = min(k, len(self.stack)) - 1
        if i >= 0:
            self.increment_arr[i] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)