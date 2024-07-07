class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        # Initialize a dictionary to keep track of the indices and corresponding characters
        index_to_char = {i: letter for i, letter in enumerate(s)}

        # Convert the string into a list of characters for in-place modification
        encrypted_chars = list(s)

        # Loop through each character in the string
        for i in range(len(s)):
            # Calculate the new index after shifting by k positions
            new_index = (i + k) % len(s)
            # Assign the character at the new index to the current position
            encrypted_chars[i] = index_to_char[new_index]

        # Join the list of characters to form the encrypted string
        return "".join(encrypted_chars)
