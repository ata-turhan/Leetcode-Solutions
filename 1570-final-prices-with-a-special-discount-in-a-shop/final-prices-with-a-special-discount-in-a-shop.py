class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discounted_prices = prices.copy()

        for i in range(len(discounted_prices)-1):
            for j in range(i + 1, len(discounted_prices)):
                if discounted_prices[j] <= discounted_prices[i]:
                    discounted_prices[i] -= discounted_prices[j]
                    break

        return discounted_prices