class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return str(int(n) - 1)
        
        # Candidates list
        candidates = set()
        
        # Edge case: 1000...0001 -> 999...999 and 1000...0001 + 2 -> 1000...0001
        candidates.add(str(10 ** (length - 1) - 1))
        candidates.add(str(10 ** length + 1))
        
        # Take the prefix of the number and form the base palindrome candidates
        prefix = int(n[:(length + 1) // 2])
        
        for diff in [-1, 0, 1]:
            new_prefix = str(prefix + diff)
            if length % 2 == 0:
                candidate = new_prefix + new_prefix[::-1]
            else:
                candidate = new_prefix + new_prefix[:-1][::-1]
            candidates.add(candidate)
        
        # Remove the original number itself from candidates
        candidates.discard(n)
        
        # Find the closest by absolute difference, and in case of tie, the smallest value
        closest = min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))
        
        return closest
