from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        """
        Matches the strongest possible players with trainers such that
        each trainer's capacity is >= the player's capability.

        Returns the maximum number of possible matches.
        """
        # Sort both lists in ascending order to allow greedy pairing from the strongest
        players.sort()
        trainers.sort()

        player_idx = len(players) - 1
        trainer_idx = len(trainers) - 1
        match_count = 0

        # Greedily match the strongest available trainer to the strongest unmatched player
        while player_idx >= 0 and trainer_idx >= 0:
            if players[player_idx] <= trainers[trainer_idx]:
                match_count += 1
                trainer_idx -= 1  # Trainer is used
            # Whether matched or not, move to the next player
            player_idx -= 1

        return match_count
