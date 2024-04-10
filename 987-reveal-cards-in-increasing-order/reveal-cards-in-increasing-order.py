from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Sort the deck
        deck.sort()
        n = len(deck)
        queue = deque(range(n))
        result = [0] * n
        
        # Iterate until all cards are revealed
        for card in deck:
            # Take the top card of the deck and reveal it
            idx = queue.popleft()
            result[idx] = card
            
            # If there are remaining cards, move the next top card to the back of the queue
            if queue:
                queue.append(queue.popleft())
        
        return result
