class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Initialize the list of friends
        friends = list(range(1, n + 1))
        current_index = 0  # This is the index of the friend to be removed

        # Continue removing friends until only one friend remains
        while len(friends) > 1:
            # Calculate the index of the next friend to be removed
            current_index = (current_index + k - 1) % len(friends)
            # Remove the friend at the calculated index
            del friends[current_index]

        # Return the last remaining friend
        return friends[0]
