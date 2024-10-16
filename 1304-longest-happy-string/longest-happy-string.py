import heapq
from typing import List

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Create a max heap (use negative counts for max heap behavior)
        char_counts = []
        if a > 0:
            char_counts.append([-a, "a"])
        if b > 0:
            char_counts.append([-b, "b"])
        if c > 0:
            char_counts.append([-c, "c"])
        heapq.heapify(char_counts)

        result = []

        while char_counts:
            # Pop the character with the highest remaining count
            count, char = heapq.heappop(char_counts)
            count = -count  # Convert back to positive

            # If the last two characters are the same, we must use another character
            if len(result) >= 2 and result[-2:] == [char] * 2:
                if not char_counts:
                    break  # No other characters to use, end the loop
                # Use the second most frequent character
                second_count, second_char = heapq.heappop(char_counts)
                second_count = -second_count
                result.append(second_char)
                # If there are more of this character, push it back to the heap
                if second_count > 1:
                    heapq.heappush(char_counts, [-(second_count - 1), second_char])
                # Push the original character back to the heap
                heapq.heappush(char_counts, [-count, char])
            else:
                # Append the most frequent character to the result
                result.append(char)
                # If more of this character remains, push it back to the heap
                if count > 1:
                    heapq.heappush(char_counts, [-(count - 1), char])

        return "".join(result)
