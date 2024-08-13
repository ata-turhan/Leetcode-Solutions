from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index: int, candidates: List[int], target: int, comb: List[int]) -> List[List[int]]:
            # Base case: If target is zero, we've found a valid combination
            if target == 0:
                return [comb[:]]  # Return a copy of the current combination
            
            # Base case: If we've reached the end of the list, return an empty list
            if index == len(candidates):
                return []
            
            results = []
            
            # Skip any candidate greater than the target since it's not usable
            if candidates[index] > target:
                return []
            
            # Include the current candidate and continue searching
            comb.append(candidates[index])
            results += dfs(index + 1, candidates, target - candidates[index], comb)
            comb.pop()  # Backtrack by removing the last added candidate

            # Skip duplicates to avoid repeated combinations
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1

            # Exclude the current candidate and continue searching
            results += dfs(index + 1, candidates, target, comb)
            
            return results
        
        candidates.sort()  # Sort candidates to handle duplicates and optimization
        return dfs(0, candidates, target, [])

