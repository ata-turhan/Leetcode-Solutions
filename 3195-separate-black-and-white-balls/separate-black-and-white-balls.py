class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps = 0
        left_black_count = 1  # Count of '1's from the left side

        # Traverse the string from right to left
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                # Calculate swaps needed and update the left_black_count
                swaps += (len(s) - left_black_count - i)
                left_black_count += 1
        
        return swaps
