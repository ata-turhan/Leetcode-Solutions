class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        players_in_a_round = n - 1  # Number of players involved in a full round
        complete_rounds = time // players_in_a_round  # Number of complete rounds
        remaining_time = time % players_in_a_round  # Remaining time after complete rounds

        # Determine the position based on whether the number of complete rounds is even or odd
        if complete_rounds % 2 == 0:
            # If the number of complete rounds is even, the pillow moves forward
            return remaining_time + 1
        else:
            # If the number of complete rounds is odd, the pillow moves backward
            return n - remaining_time
