class Solution:
    def numberToWords(self, num: int) -> str:
        # Handle special case for zero
        if num == 0:
            return "Zero"

        # Define mappings for number words
        units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", 
                 "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        # Convert numbers less than 1000 to words
        def numberToWordsBelow1000(n):
            if n == 0:
                return ""
            elif n < 20:
                return units[n] + " "  # Directly map numbers 1-19
            elif n < 100:
                return tens[n // 10] + " " + numberToWordsBelow1000(n % 10)  # Handle tens and units
            else:
                return units[n // 100] + " Hundred " + numberToWordsBelow1000(n % 100)  # Handle hundreds

        result = ""
        # Process each group of thousands
        for i in range(len(thousands)):
            # Check if the current group (e.g., hundreds, thousands) is non-zero
            if num % 1000 != 0:
                # Convert current group to words and append the appropriate thousand's place
                result = numberToWordsBelow1000(num % 1000) + thousands[i] + " " + result
            # Move to the next group of thousands
            num //= 1000
        
        # Remove trailing spaces and return the final result
        return result.strip()
