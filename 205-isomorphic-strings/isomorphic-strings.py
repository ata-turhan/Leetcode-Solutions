class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # If lengths of 's' and 't' are not equal, they cannot be isomorphic
        if len(s) != len(t):
            return False
        
        # Dictionary to store character mappings from 's' to 't'
        char_map = {}
        # Set to keep track of already mapped characters in 't'
        mapped_chars = set()
        
        # Iterating through each character in 's' and 't'
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            # If character from 's' is already mapped
            if char_s in char_map:
                # Check if the mapping is consistent
                if char_map[char_s] != char_t:
                    return False
            else:
                # If character from 's' is not mapped, but the character from 't' is already mapped to another character in 's'
                if char_t in mapped_chars:
                    return False
                # Add the mapping from 's' to 't'
                char_map[char_s] = char_t
                # Add the character from 't' to the set of mapped characters
                mapped_chars.add(char_t)
        
        # If all characters are successfully mapped without inconsistencies, return True
        return True
