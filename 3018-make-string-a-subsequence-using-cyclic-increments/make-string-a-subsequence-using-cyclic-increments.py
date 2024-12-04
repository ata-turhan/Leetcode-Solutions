class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        subsequence_index = 0
        
        # Iterate through each character in str1
        for char in str1:
            # Check if the current character matches the required character in str2
            # or if it can be incremented cyclically to match
            if (char == str2[subsequence_index] or 
                chr((ord(char) - ord('a') + 1) % 26 + ord('a')) == str2[subsequence_index]):
                subsequence_index += 1
                
                # If the entire str2 is matched, return True
                if subsequence_index == len(str2):
                    return True
        
        # Return whether all characters of str2 were matched
        return subsequence_index == len(str2)
