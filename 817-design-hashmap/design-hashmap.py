class MyHashMap:

    def __init__(self):
        self.arr = [-1] * (10**6 + 1)
        

    def put(self, key: int, value: int) -> None:
        self.arr[key] = value

        

    def get(self, key: int) -> int:
        return self.arr[key]
        

    def remove(self, key: int) -> None:
        self.arr[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)