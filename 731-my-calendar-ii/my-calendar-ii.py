from bisect import insort

class MyCalendarTwo:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        # Insert start and end points with delta +1 for start and -1 for end
        insort(self.bookings, (start, 1))
        insort(self.bookings, (end, -1))

        # Variable to track ongoing events
        running_sum = 0

        for _, delta in self.bookings:
            running_sum += delta
            if running_sum > 2:  # If more than 2 bookings overlap, we need to rollback
                # Rollback the insertion by removing the last inserted events
                self.bookings.remove((start, 1))
                self.bookings.remove((end, -1))
                return False

        return True
