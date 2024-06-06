import heapq
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Determines if the hand can be rearranged into groups of consecutive cards of groupSize.
        
        :param hand: List[int] - A list of integers representing the hand of cards.
        :param groupSize: int - The size of each group.
        :return: bool - True if the hand can be rearranged into groups, False otherwise.
        """
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for num in hand:
            count[num] = 1 + count.get(num, 0)  # Count the frequency of each card

        min_heap = list(count.keys())
        heapq.heapify(min_heap)  # Create a min-heap of the card values

        while min_heap:
            first = min_heap[0]  # Get the smallest card value
            # Try to form a group starting from the smallest card value
            for i in range(first, first + groupSize):
                if i not in count or count[i] == 0:
                    return False  # If the card is missing or already used up, return False
                count[i] -= 1
                if count[i] == 0:
                    if i != min_heap[0]:
                        return False  # If the card is not the smallest, return False
                    heapq.heappop(min_heap)  # Remove the smallest card value from the heap

        return True

# Example usage:
# sol = Solution()
# print(sol.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))  # Output: True
# print(sol.isNStraightHand([1,2,3,4,5], 4))          # Output: False
