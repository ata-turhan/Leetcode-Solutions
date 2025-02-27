class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        # Create a mapping from each number to its index for O(1) look-ups.
        index = {x: i for i, x in enumerate(arr)}
        
        # dp[(i, j)] will store the length of the Fibonacci-like subsequence ending with arr[i] and arr[j].
        # Initially, every pair (i, j) is set to 2 (the minimal length for a potential sequence).
        dp = {}
        max_len = 0  # Track the maximum length found
        
        # Iterate through all pairs (i, j) with i < j.
        for j in range(n):
            for i in range(j):
                # The potential previous number in the Fibonacci sequence should be arr[j] - arr[i].
                k = index.get(arr[j] - arr[i])
                
                # Check if this potential number exists and if its index is less than i.
                if k is not None and k < i:
                    # If a valid previous element exists, extend the sequence.
                    # If (k, i) is not in dp, it means the length was 2, so we add 1.
                    dp[(i, j)] = dp.get((k, i), 2) + 1
                    max_len = max(max_len, dp[(i, j)])
                else:
                    # Otherwise, initialize the pair (i, j) as a potential sequence of length 2.
                    dp[(i, j)] = 2
                    
        # Only sequences of length 3 or more count as valid Fibonacci-like subsequences.
        return max_len if max_len >= 3 else 0