class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k  # Use exactly k elements
        self.deque = [0] * self.capacity  # Initialize deque with zeros
        self.front = self.capacity  # Front pointer
        self.rear = 0  # Rear pointer
        self.size = 0  # Tracks current number of elements

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.capacity  # Move front pointer back
        self.deque[self.front] = value  # Insert the value at front
        self.size += 1  # Increment size
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.rear] = value  # Insert the value at rear
        self.rear = (self.rear + 1) % self.capacity  # Move rear pointer forward
        self.size += 1  # Increment size
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity  # Move front pointer forward to delete
        self.size -= 1  # Decrement size
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.capacity  # Move rear pointer back to delete
        self.size -= 1  # Decrement size
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]  # Return front element

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1) % self.capacity]  # Return rear element

    def isEmpty(self) -> bool:
        return self.size == 0  # Deque is empty when size is 0

    def isFull(self) -> bool:
        return self.size == self.capacity  # Deque is full when size equals capacity
