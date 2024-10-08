class Solution:
    def minSwaps(self, s: str) -> int:
        imbalance = 0
        max_imbalance = 0
        
        # Traverse the string to find the maximum imbalance
        for char in s:
            if char == '[':
                imbalance -= 1  # Opening bracket decreases imbalance
            else:
                imbalance += 1  # Closing bracket increases imbalance
            
            # We are only concerned when there are more closing brackets than opening
            max_imbalance = max(max_imbalance, imbalance)
        
        # The number of swaps needed is max_imbalance divided by 2, rounded up
        return (max_imbalance + 1) // 2

        