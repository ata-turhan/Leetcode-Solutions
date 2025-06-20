from typing import List

class Solution:
    def maxDistance(self, moves: str, k: int) -> int:
        """
        Computes the maximum “Manhattan” distance reachable at any prefix of the move sequence,
        given you can use up to k “reverse” moves (i.e., cancel one N/S or E/W pair to extend distance by 2).
        
        For each prefix of the string `moves`, we track counts of N, S, E, W. The base distance is
        |N−S| + |E−W|. We can “reverse” up to k pairs among the balanced moves (min(N,S) + min(E,W)),
        each reversal adds 2 to the distance. We take the maximum over all prefixes.
        """
        north = south = east = west = 0
        max_distance = 0

        for ch in moves:
            if ch == 'N':
                north += 1
            elif ch == 'S':
                south += 1
            elif ch == 'E':
                east += 1
            elif ch == 'W':
                west += 1

            # Base Manhattan distance for this prefix
            base = abs(north - south) + abs(east - west)
            # Total pairs available to reverse
            reversible_pairs = min(north, south) + min(east, west)
            # We can only use up to k reversals
            used_reversals = min(k, reversible_pairs)
            # Each reversal adds 2 to the distance
            candidate = base + 2 * used_reversals

            if candidate > max_distance:
                max_distance = candidate

        return max_distance
