class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # Function to calculate the minimum distance between two ring indices
        def min_dist(total_len, idx1, idx2):
            dist1 = abs(idx1 - idx2)
            dist2 = total_len - dist1
            return min(dist1, dist2)

        # Memoized DFS function to find the minimum steps to type the key
        @cache
        def dfs(ring, key, ring_idx, key_idx):
            # Base case: If all characters in the key are typed, return 0
            if key_idx == len(key):
                return 0
            # Initialize the minimum steps to infinity
            min_val = float("inf")
            # Iterate through each index of the ring
            for i in range(len(ring)):
                # Check if the character at the current index of the ring matches the character at the current index of the key
                if ring[i] == key[key_idx]:
                    # Calculate the minimum steps required to type the remaining key characters recursively
                    min_val = min(min_val, min_dist(len(ring), ring_idx, i) + 1 + dfs(ring, key, i, key_idx + 1))
            # Return the minimum steps required
            return min_val
        
        # Call the memoized DFS function with initial parameters
        return dfs(ring, key, 0, 0)
