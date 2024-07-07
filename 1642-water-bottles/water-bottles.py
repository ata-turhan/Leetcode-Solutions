class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = 0
        full_bottles = numBottles
        empty_bottles = 0

        while full_bottles > 0:
            # Drink all full bottles
            total_drunk += full_bottles
            # Calculate new full bottles by exchanging empty bottles
            new_bottles = (full_bottles + empty_bottles)
            full_bottles = new_bottles // numExchange
            empty_bottles = new_bottles % numExchange

        return total_drunk
