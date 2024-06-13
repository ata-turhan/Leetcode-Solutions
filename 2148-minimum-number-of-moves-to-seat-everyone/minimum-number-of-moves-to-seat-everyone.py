class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        moves = 0

        for se, st in zip(seats, students):
            moves += abs(se-st)

        return moves        