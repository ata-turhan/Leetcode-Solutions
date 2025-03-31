class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        # If only one bag is needed, the score is fixed.
        if k == 1:
            return 0

        # Calculate the candidate contributions for each possible cut.
        candidates = []
        for i in range(1, n):
            candidates.append(weights[i-1] + weights[i])
        
        # Sort the candidate contributions.
        candidates.sort()

        # Sum up the smallest and largest (k-1) candidate values.
        min_sum = sum(candidates[:k-1])
        max_sum = sum(candidates[-(k-1):])
        
        # The difference between the maximum and minimum scores.
        return max_sum - min_sum
