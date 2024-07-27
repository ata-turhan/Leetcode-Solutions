class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        alpha_letters = 26
        upper_bound = 10**7
        distances = [[upper_bound] * alpha_letters for _ in range(alpha_letters)]
        for i in range(alpha_letters):
            distances[i][i] = 0
        for org, cha, cos in zip(original, changed, cost):
            i = ord(org) - ord("a")
            j = ord(cha) - ord("a")
            distances[i][j] = min(distances[i][j], cos)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

        total_cost = 0
        for s, t in zip(source, target):
            i = ord(s) - ord("a")
            j = ord(t) - ord("a")
            if distances[i][j] == upper_bound:
                return -1
            else:
                total_cost += distances[i][j]
        return total_cost
        