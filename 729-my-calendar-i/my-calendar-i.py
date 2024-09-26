from sortedcontainers import SortedList

class MyCalendar:
    def __init__(self):
        # Initialize an empty sorted list to store bookings
        self.bookings = SortedList()

    def book(self, start: int, end: int) -> bool:
        # Find the position where the current start would fit in the sorted list
        idx = self.bookings.bisect_left((start, end))
        
        # Check if there is an overlap with the previous event
        if idx > 0 and self.bookings[idx-1][1] > start:
            return False
        
        # Check if there is an overlap with the next event
        if idx < len(self.bookings) and self.bookings[idx][0] < end:
            return False
        
        # If no overlap, add the booking
        self.bookings.add((start, end))
        return True
