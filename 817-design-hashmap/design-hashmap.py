class MyHashMap:

    def __init__(self):
        # Initialize an array to represent the HashMap, initially all set to -1
        self.arr = [-1] * (10**6 + 1)

    def put(self, key: int, value: int) -> None:
        # Store the value at the index corresponding to the key
        self.arr[key] = value

    def get(self, key: int) -> int:
        # Return the value stored at the index corresponding to the key
        return self.arr[key]

    def remove(self, key: int) -> None:
        # Remove the value stored at the index corresponding to the key by setting it to -1
        self.arr[key] = -1



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)