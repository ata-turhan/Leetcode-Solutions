from sortedcontainers import SortedList

class MedianFinder:
    def __init__(self):
        """
        Initialize the MedianFinder object.
        """
        self.arr = SortedList()  # Initialize an empty SortedList to store numbers

    def addNum(self, num: int) -> None:
        """
        Adds a number into the data structure.
        
        :param num: int - The number to be added.
        """
        self.arr.add(num)  # Add the number to the sorted list

    def findMedian(self) -> float:
        """
        Finds the median of all elements added so far.
        
        :return: float - The median of the current elements.
        """
        length = len(self.arr)  # Get the number of elements
        if length & 1 == 1:  # If the number of elements is odd
            return self.arr[length // 2]  # Return the middle element
        else:  # If the number of elements is even
            # Return the average of the two middle elements
            return (self.arr[length // 2] + self.arr[length // 2 - 1]) / 2

# Example usage:
# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# print(obj.findMedian())  # Output: 1.5
# obj.addNum(3)
# print(obj.findMedian())  # Output: 2
