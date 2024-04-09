class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        idx = k
        # Iterate until all tickets are purchased at position k
        while True:
            # Check if all tickets are purchased at position k
            if idx == 0 and tickets[idx] == 1:
                return time + 1  # Return the total time taken
            # If the last ticket is being bought, just remove it
            if tickets[0] == 1:
                tickets.pop(0)
            else:
                # If not, decrease the ticket number and move it from the front to the end of the queue
                el = tickets.pop(0)
                tickets.append(el - 1)
            # Update the current k index
            idx = (idx - 1) % len(tickets)
            time += 1  # Increment time after each purchase or movement
