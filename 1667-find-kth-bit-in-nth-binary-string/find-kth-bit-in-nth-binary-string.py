class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Function to generate the nth string
        def generateNthString(n: int) -> str:
            if n == 1:
                return "0"
            
            # Recursively generate the previous string
            prev_string = generateNthString(n - 1)
            
            # Invert and reverse the previous string
            inverted_reversed = ''.join('1' if char == '0' else '0' for char in reversed(prev_string))
            
            # Concatenate previous string + "1" + inverted and reversed string
            return prev_string + "1" + inverted_reversed
        
        # Generate the nth string and return the k-th bit
        nth_string = generateNthString(n)
        return nth_string[k - 1]
