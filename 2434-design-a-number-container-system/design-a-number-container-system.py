import heapq

class NumberContainers:

    def __init__(self):
        # Maps index to its current number.
        self.index_to_number = {}
        # Maps each number to a min-heap of indices containing that number.
        self.number_to_heap = {}

    def change(self, index: int, number: int) -> None:
        # If the index already contains a number, we simply update the mapping.
        # Lazy deletion: the old index remains in the heap and will be cleaned up during find().
        if index in self.index_to_number:
            # No immediate removal from number_to_heap is necessary.
            pass

        # Update the mapping for this index.
        self.index_to_number[index] = number

        # Ensure the heap for this number exists.
        if number not in self.number_to_heap:
            self.number_to_heap[number] = []
        
        # Add the index to the heap corresponding to the new number.
        heapq.heappush(self.number_to_heap[number], index)

    def find(self, number: int) -> int:
        # If the number is not present, return -1.
        if number not in self.number_to_heap:
            return -1
        
        heap = self.number_to_heap[number]
        
        # Lazy deletion: Remove indices from the heap that no longer map to the given number.
        while heap and self.index_to_number.get(heap[0], None) != number:
            heapq.heappop(heap)
        
        # If the heap is empty after cleaning, return -1.
        return heap[0] if heap else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index, number)
# param_2 = obj.find(number)
