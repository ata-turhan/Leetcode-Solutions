class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.i = 0
        self.j = 0
        

    def next(self) -> int:
        while self.i < len(self.vec) and self.j >= len(self.vec[self.i]):
            self.i += 1
            self.j = 0

        if self.i == len(self.vec) or self.j >= len(self.vec[self.i]):
            return None

        self.j += 1
        return self.vec[self.i][self.j-1]
        

    def hasNext(self) -> bool:
        previous_i = self.i
        previous_j = self.j

        res = False
        if self.next() is not None:
            res = True
        
        self.i = previous_i
        self.j = previous_j

        return res
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()