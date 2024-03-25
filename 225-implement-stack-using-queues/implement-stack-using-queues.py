from collections import deque

class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.empty():
            # Move all elements except the last one to the back
            for _ in range(len(self.stack) - 1):
                self.stack.append(self.stack.popleft())
            # Retrieve and return the last element (simulating pop)
            return self.stack.popleft()

    def top(self) -> int:
        if not self.empty():
            # Return the last element without removing it (simulating top)
            return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack