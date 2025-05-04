class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        domino_counts = defaultdict(int)

        for domino in dominoes:
            domino_counts["".join(map(str, sorted(domino)))] += 1

        pair_count = 0

        for value in domino_counts.values():
            pair_count += (value * (value - 1)) // 2

        return pair_count
        