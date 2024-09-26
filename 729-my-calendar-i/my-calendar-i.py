import bisect

class MyCalendar:

    def __init__(self):
        self.bookings = []  # To store (start, end) pairs of bookings

    def book(self, start: int, end: int) -> bool:
        # Iterate through the existing bookings to check for overlap
        for s, e in self.bookings:
            # Check if there is any overlap with the existing booking
            if max(s, start) < min(e, end):
                return False

        # If no overlap, append the new booking
        self.bookings.append((start, end))
        return True
