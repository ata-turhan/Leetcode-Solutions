from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, it's impossible to find a permutation of s1 in s2
        if len(s1) > len(s2):
            return False

        # Count frequency of characters in s1 and the first window in s2 (size of len(s1))
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])
        
        matched_chars = 0  # To keep track of how many characters match
        required_matches = len(s1_count)  # Number of unique characters in s1 that need to match

        # Initialize the count of matches in the first window
        for char in s1_count:
            if s1_count[char] <= s2_count[char]:
                matched_chars += 1

        # If the first window is a valid permutation, return True
        if matched_chars == required_matches:
            return True

        # Slide the window across s2, checking for valid permutations
        for i in range(len(s1), len(s2)):
            outgoing_char = s2[i - len(s1)]  # Character that's sliding out of the window
            incoming_char = s2[i]  # Character that's sliding into the window

            # Update the count for the outgoing character
            if s2_count[outgoing_char] == s1_count[outgoing_char]:
                matched_chars -= 1
            s2_count[outgoing_char] -= 1

            # Update the count for the incoming character
            if s2_count[incoming_char] == s1_count[incoming_char] - 1:
                matched_chars += 1
            s2_count[incoming_char] += 1

            # If all characters match, return True
            if matched_chars == required_matches:
                return True

        return False
