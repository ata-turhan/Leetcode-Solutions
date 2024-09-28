class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k + 1  # Use k + 1 to differentiate full and empty states
        self.deque = [0] * self.capacity  # Initialize deque with zeros
        self.front = 0  # Front pointer
        self.rear = 0  # Rear pointer

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity  # Move front pointer back
        self.deque[self.front] = value  # Insert the value at front
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.rear] = value  # Insert the value at rear
        self.rear = (self.rear + 1) % self.capacity  # Move rear pointer forward
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity  # Move front pointer forward to delete
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity  # Move rear pointer back to delete
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]  # Return front element

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1 + self.capacity) % self.capacity]  # Return rear element

    def isEmpty(self) -> bool:
        return self.front == self.rear  # Deque is empty if front and rear are the same

    def isFull(self) -> bool:
        return (self.rear + 1) % self.capacity == self.front  # Deque is full if next rear is equal to front
