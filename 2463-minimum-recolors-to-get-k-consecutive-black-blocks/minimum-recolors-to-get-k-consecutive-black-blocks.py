class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """Finds the minimum number of recolors needed to get k consecutive 'B' blocks."""
        
        # Initialize the minimum recolors needed to k (worst case scenario)
        min_recolors = k
        
        # Count initial 'W' in the first window of size k
        white_count = blocks[:k].count("W")
        min_recolors = min(min_recolors, white_count)
        
        # Sliding window approach to update the count dynamically
        for right in range(k, len(blocks)):
            if blocks[right - k] == "W":  # Remove outgoing element
                white_count -= 1
            if blocks[right] == "W":  # Add incoming element
                white_count += 1
            
            min_recolors = min(min_recolors, white_count)

        return min_recolors
