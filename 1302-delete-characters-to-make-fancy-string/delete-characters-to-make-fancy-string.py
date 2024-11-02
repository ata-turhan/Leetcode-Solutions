class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []

        # Iterate through each character in the string
        for char in s:
            # If result has fewer than two characters, simply add the current character
            if len(result) < 2:
                result.append(char)
            else:
                # Check if the last two characters are the same as the current character
                if char == result[-1] == result[-2]:
                    continue  # Skip appending the character to avoid three consecutive duplicates
                else:
                    result.append(char)
        
        # Join and return the list as a final fancy string
        return "".join(result)
