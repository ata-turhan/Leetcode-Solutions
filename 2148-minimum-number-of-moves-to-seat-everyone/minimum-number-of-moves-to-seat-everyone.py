from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()  # Sort the seats array
        students.sort()  # Sort the students array

        moves = 0

        # Calculate the total moves required by matching each student to the closest seat
        for seat, student in zip(seats, students):
            moves += abs(seat - student)

        return moves
