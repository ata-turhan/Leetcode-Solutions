from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        Calculate the final discounted prices for each product. A discount is applied 
        if a smaller or equal price exists later in the list.

        :param prices: List of integers representing the original prices.
        :return: List of integers with final discounted prices.
        """
        final_prices = prices.copy()  # Copy of prices to store final discounted prices

        # Iterate through each price
        for current_index in range(len(final_prices) - 1):
            # Find the first smaller or equal price after the current index
            for next_index in range(current_index + 1, len(final_prices)):
                if final_prices[next_index] <= final_prices[current_index]:
                    # Apply the discount and stop further checks
                    final_prices[current_index] -= final_prices[next_index]
                    break

        return final_prices
