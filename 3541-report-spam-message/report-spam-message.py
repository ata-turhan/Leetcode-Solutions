from typing import List

class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        # Convert bannedWords list to a set for O(1) lookups
        banned_set = set(bannedWords)
        banned_count = 0

        # Iterate over each word in the message
        for word in message:
            if word in banned_set:
                banned_count += 1
            # If at least two banned words are found, return True early
            if banned_count >= 2:
                return True

        # Return False if fewer than two banned words are found
        return False
