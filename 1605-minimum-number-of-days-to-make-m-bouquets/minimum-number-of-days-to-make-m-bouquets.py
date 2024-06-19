from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # If it's impossible to get the needed bouquets, return -1 immediately.
        if m * k > len(bloomDay):
            return -1
        
        def canMakeBouquets(days: int) -> bool:
            # Function to check if we can make m bouquets in 'days' days
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:  # If we have enough flowers for a bouquet
                        bouquets += 1
                        flowers = 0  # Reset the flowers counter
                else:
                    flowers = 0  # Reset the flowers counter if current bloom day is greater than days
                if bouquets >= m:  # If we already have enough bouquets
                    return True
            return False
        
        left, right = min(bloomDay), max(bloomDay)
        
        while left < right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                right = mid  # Try to find a smaller number of days
            else:
                left = mid + 1  # Increase the number of days
        
        return left
