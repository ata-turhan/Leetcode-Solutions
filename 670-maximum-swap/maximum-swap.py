class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number into a list of digits
        num_arr = list(map(int, str(num)))
        
        # Record the last occurrence of each digit
        last_occurrence = {digit: i for i, digit in enumerate(num_arr)}
        
        # Traverse the digits of the number
        for i in range(len(num_arr)):
            # Check if there's a larger digit later in the number
            for d in range(9, num_arr[i], -1):
                if last_occurrence.get(d, -1) > i:
                    # Swap the current digit with the largest possible digit
                    num_arr[i], num_arr[last_occurrence[d]] = num_arr[last_occurrence[d]], num_arr[i]
                    # Convert the list of digits back to an integer and return
                    return int("".join(map(str, num_arr)))
        
        # If no swap was made, return the original number
        return num
