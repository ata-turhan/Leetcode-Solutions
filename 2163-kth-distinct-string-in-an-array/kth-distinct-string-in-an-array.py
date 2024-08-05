class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Dictionary to store the frequency of each string
        freqs = defaultdict(int)
        
        # Count the occurrences of each string
        for word in arr:
            freqs[word] += 1
        
        # Variable to keep track of the number of distinct strings found
        distinct_count = 0
        
        # Iterate over the array to find the k-th distinct string
        for word in arr:
            if freqs[word] == 1:  # Check if the string appears exactly once
                distinct_count += 1  # Increment the count of distinct strings
                if distinct_count == k:  # If we've found the k-th distinct string
                    return word  # Return the k-th distinct string
        
        # If there aren't enough distinct strings, return an empty string
        return ""
