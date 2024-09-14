class Solution:
    def convertDateToBinary(self, date: str) -> str:
        # Split the input date by "-" to separate year, month, and day
        date_parts: list[str] = date.split("-")
        binary_date_parts: list[str] = []

        # Convert each part of the date to binary and remove the '0b' prefix
        for part in date_parts:
            binary_representation: str = bin(int(part))[2:]
            binary_date_parts.append(binary_representation)

        # Join the binary date parts with "-" to form the final string
        return "-".join(binary_date_parts)
