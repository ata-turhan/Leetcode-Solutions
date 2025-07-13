class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i, j = len(players) - 1, len(trainers) - 1
        matches = 0

        while i >= 0 and j >= 0:
            if players[i] <= trainers[j]:
                matches += 1
                i -= 1
                j -= 1
            else:
                i -= 1
        
        return matches
        