class Solution:
    def countAndSay(self, n: int) -> str:
        # Start with the first number in the sequence
        num_sequence = ["1"]
        
        # Iterate through the sequence to generate the next numbers
        for i in range(n - 1):
            count = 1  # Initialize count for consecutive digits
            prev_digit = num_sequence[0]  # Initialize the previous digit
            new_sequence = []  # Initialize the new sequence
            
            # Iterate through the digits in the current number
            for j in range(1, len(num_sequence)):
                # If the current digit is the same as the previous one, increment the count
                if num_sequence[j] == prev_digit:
                    count += 1
                # If the current digit is different from the previous one, add the count and digit to the new sequence
                else:
                    new_sequence.extend(list(str(count)))  # Add the count as separate digits
                    new_sequence.append(prev_digit)  # Add the previous digit
                    count = 1  # Reset the count for the new digit
                    prev_digit = num_sequence[j]  # Update the previous digit
                
            # Add the count and digit of the last group of digits to the new sequence
            new_sequence.extend(list(str(count)))
            new_sequence.append(prev_digit)
            
            # Update the number sequence with the new sequence
            num_sequence = new_sequence
        
        # Convert the number sequence to a string and return it
        return "".join(num_sequence)
