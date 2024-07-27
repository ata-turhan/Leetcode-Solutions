class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Constants
        ALPHA_LETTERS = 26  # Number of letters in the alphabet
        UPPER_BOUND = 10**7  # Upper bound for distances
        
        # Initialize the distance matrix with upper_bound
        distances = [[UPPER_BOUND] * ALPHA_LETTERS for _ in range(ALPHA_LETTERS)]
        
        # Set the distance from each character to itself to 0
        for i in range(ALPHA_LETTERS):
            distances[i][i] = 0
        
        # Populate the initial distances based on the given transformations
        for org, cha, cos in zip(original, changed, cost):
            i = ord(org) - ord("a")
            j = ord(cha) - ord("a")
            distances[i][j] = min(distances[i][j], cos)
        
        # Floyd-Warshall algorithm to find the minimum cost between all pairs of characters
        for k in range(ALPHA_LETTERS):
            for i in range(ALPHA_LETTERS):
                for j in range(ALPHA_LETTERS):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
        
        # Calculate the total transformation cost from source to target
        total_cost = 0
        for s, t in zip(source, target):
            i = ord(s) - ord("a")
            j = ord(t) - ord("a")
            # If there's no valid transformation, return -1
            if distances[i][j] == UPPER_BOUND:
                return -1
            else:
                total_cost += distances[i][j]
        
        return total_cost
