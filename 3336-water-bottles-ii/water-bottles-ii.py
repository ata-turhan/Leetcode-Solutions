class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        # Initialize variables
        total_bottles_drank = 0  # Total number of bottles drunk
        full_bottles = numBottles  # Number of full bottles
        empty_bottles = 0  # Number of empty bottles
        
        # Exchange full bottles for empty bottles until there are no more full bottles left
        while full_bottles > 0 or empty_bottles >= numExchange:
            # Add full bottles to the total number drunk
            total_bottles_drank += full_bottles
            
            # Exchange full bottles for empty bottles
            empty_bottles += full_bottles
            full_bottles = 0
            
            # Calculate the number of new full bottles obtained from the empty bottles
            while empty_bottles >= numExchange:
                # Update the number of empty bottles after exchange
                empty_bottles -= numExchange
                numExchange += 1

                full_bottles = 1
                total_bottles_drank += full_bottles
                
                # Update the number of empty bottles left for the next exchange
                empty_bottles += full_bottles
                full_bottles = 0

        return total_bottles_drank
