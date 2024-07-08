class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n+1))
        removed_index = 0
        while len(friends) > 1:
            removed_index = (removed_index + k - 1) % len(friends)
            del friends[removed_index]
            removed_index = removed_index % len(friends)

        return friends[0]
        