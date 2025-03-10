import bisect
from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # Define vowels for quick membership testing.
        vowels = set("aeiou")
        n = len(word)
        
        # Build the prefix array for consonant counts.
        # C[i] represents the number of consonants in word[0:i].
        C = [0] * (n + 1)
        for i, ch in enumerate(word):
            # Increase count only if the character is a consonant.
            C[i+1] = C[i] + (0 if ch in vowels else 1)
        
        # Create a dictionary mapping each prefix consonant count
        # to the list of indices where that count occurs.
        pos_by_prefix = defaultdict(list)
        for i, val in enumerate(C):
            pos_by_prefix[val].append(i)
        
        # We'll maintain the last seen index for each vowel.
        lastOccurrence = {v: -1 for v in vowels}
        
        total = 0
        # Iterate over every possible end index 'r' for the substring.
        for r, ch in enumerate(word):
            # If current character is a vowel, update its last occurrence.
            if ch in vowels:
                lastOccurrence[ch] = r
            
            # Only consider substrings ending at r if every vowel has appeared at least once.
            if any(lastOccurrence[v] == -1 for v in vowels):
                continue
            
            # For the current substring ending at r, 
            # let M be the smallest last occurrence index among the vowels.
            # This ensures that any valid starting index l must satisfy l <= M,
            # so that word[l:r+1] contains every vowel.
            M = min(lastOccurrence.values())
            
            # We require exactly k consonants in the substring word[l:r+1].
            # Since C[r+1] is the consonant count in word[0:r+1],
            # we need C[r+1] - C[l] == k, or equivalently, C[l] == C[r+1] - k.
            needed = C[r+1] - k
            
            # If no prefix index has the required consonant count, skip.
            if needed not in pos_by_prefix:
                continue
            
            # Count how many indices l (in the prefix array) with C[l] == needed
            # satisfy l <= M. This is done via binary search in the sorted list.
            indices = pos_by_prefix[needed]
            count_l = bisect.bisect_right(indices, M)
            
            # Add the number of valid starting indices for this end index r.
            total += count_l
        
        return total
