from typing import List

class Solution:
    def minChanges(self, s: str) -> int:
        consecutive_counts = []  # Stores counts of consecutive identical characters
        previous_char = ""
        current_count = 0
        
        # Count consecutive characters
        for char in s:
            if char == previous_char:
                current_count += 1
            else:
                if current_count != 0:
                    consecutive_counts.append(current_count)
                previous_char = char
                current_count = 1
        consecutive_counts.append(current_count)  # Append last count

        # Calculate minimum changes needed
        changes_needed = 0
        for i in range(len(consecutive_counts)):
            # If count is odd, increment changes and adjust the next count
            if consecutive_counts[i] % 2 != 0:
                changes_needed += 1
                if i < len(consecutive_counts) - 1:
                    consecutive_counts[i + 1] += 1

        return changes_needed
