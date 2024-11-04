class Solution:
    def compressedString(self, word: str) -> str:
        """
        Compresses the input string such that consecutive characters are represented
        by the character followed by the number of times it appears consecutively.
        
        :param word: str - The input string to be compressed.
        :return: str - The compressed string.
        """
        result = []
        previous_char = ""
        count = 0

        for char in word:
            if char == previous_char:
                count += 1
                # If count reaches 9, append the compressed part and reset
                if count == 9:
                    result.append(f"{count}{previous_char}")
                    previous_char = ""
                    count = 0
            else:
                # Append the compressed part of the previous character
                if count > 0:
                    result.append(f"{count}{previous_char}")
                previous_char = char
                count = 1
        
        # Append the remaining characters
        if count != 0:
            result.append(f"{count}{previous_char}")
        
        return "".join(result)
