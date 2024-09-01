class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = []
        n = len(s)
        
        # Iterate over the string in chunks of size k
        for i in range(0, n, k):
            substr = s[i:i+k]  # Extract the substring of length k
            # Calculate the hash sum as the sum of positional values of the characters
            hash_sum = sum(ord(ch) - ord('a') for ch in substr)
            # Determine the corresponding character for the hash sum modulo 26
            hash_char = chr((hash_sum % 26) + ord('a'))
            # Append the calculated character to the result list
            result.append(hash_char)
        
        return "".join(result)
