from collections import defaultdict

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        # Create a defaultdict to store the frequency of substrings of length k
        substring_freq = defaultdict(int)
        max_freq = 0
        
        # Iterate through the word with step k
        for i in range(0, len(word), k):
            substring = word[i:i+k]
            substring_freq[substring] += 1
            max_freq = max(max_freq, substring_freq[substring])
        
        # Calculate the minimum number of operations needed to make the word k-periodic
        return len(word) // k - max_freq
