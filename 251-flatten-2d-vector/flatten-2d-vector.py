from typing import List

class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.i = 0
        self.j = 0

    def next(self) -> int:
        # Move to the next valid sublist if needed
        while self.i < len(self.vec) and self.j >= len(self.vec[self.i]):
            self.i += 1
            self.j = 0

        # If we are out of bounds, return None (indicating no more elements)
        if self.i == len(self.vec) or self.j >= len(self.vec[self.i]):
            return None

        # Return the current element and move to the next
        result = self.vec[self.i][self.j]
        self.j += 1
        return result

    def hasNext(self) -> bool:
        # Check for next valid element without changing internal state
        temp_i, temp_j = self.i, self.j
        while temp_i < len(self.vec):
            if temp_j < len(self.vec[temp_i]):
                return True
            temp_i += 1
            temp_j = 0
        return False

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
