class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Map vowels to bits
        vowel_to_bit = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
        state = 0  # Initial state where all counts are even
        max_length = 0
        state_to_index = {0: -1}  # State 0 occurs at index -1

        for i, c in enumerate(s):
            if c in vowel_to_bit:
                # Flip the bit corresponding to the vowel
                bit = vowel_to_bit[c]
                state ^= (1 << bit)
            # Check if this state has been seen before
            if state in state_to_index:
                # Update max_length if we found a longer substring
                length = i - state_to_index[state]
                max_length = max(max_length, length)
            else:
                # Record the first occurrence of this state
                state_to_index[state] = i

        return max_length