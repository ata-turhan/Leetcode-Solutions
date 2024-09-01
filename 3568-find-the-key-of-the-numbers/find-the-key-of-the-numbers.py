class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        # Convert each number to a 4-digit string, padding with zeros if necessary
        str_num1 = str(num1).zfill(4)
        str_num2 = str(num2).zfill(4)
        str_num3 = str(num3).zfill(4)

        # Initialize the key as an empty string
        key = ""

        # Iterate over each digit position (0 to 3)
        for i in range(4):
            # Find the minimum digit at the current position across the three numbers
            min_digit = min(str_num1[i], str_num2[i], str_num3[i])
            # Append the minimum digit to the key string
            key += min_digit

        # Convert the final key string back to an integer
        return int(key)
