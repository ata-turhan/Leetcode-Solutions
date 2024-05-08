class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Sort the scores in descending order
        sorted_scores = sorted(score, reverse=True)
        
        # Create a dictionary to map scores to ranks
        rank_map = {}
        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_map[s] = "Gold Medal"
            elif i == 1:
                rank_map[s] = "Silver Medal"
            elif i == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(i + 1)
        
        # Create a list to store the relative ranks
        relative_ranks = []
        for s in score:
            relative_ranks.append(rank_map[s])
        
        return relative_ranks
