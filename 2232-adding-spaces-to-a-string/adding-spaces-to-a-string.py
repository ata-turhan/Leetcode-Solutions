class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Convert the input string to a list for efficient manipulation
        result = []
        space_index = 0
        
        # Iterate through the characters in the string
        for i, char in enumerate(s):
            # If the current index matches the next space index, add a space
            if space_index < len(spaces) and i == spaces[space_index]:
                result.append(" ")
                space_index += 1
            result.append(char)  # Append the current character
        
        return "".join(result)  # Join the list into a string and return
