from bisect import bisect_right
from collections import defaultdict

class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.counts = defaultdict(int)
        self.winners = {}
        winner_count = 0
        winner = -1
        for person, time in zip(persons, times):
            self.counts[person] += 1
            if self.counts[person] >= winner_count:
                winner_count = self.counts[person]
                winner = person
            self.winners[time] = winner

    def q(self, t: int) -> int:
        idx = bisect_right(self.times, t)
        if idx == 0:
            return -1
        return self.winners[self.times[idx - 1]]
