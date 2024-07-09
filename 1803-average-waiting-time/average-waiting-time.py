class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting_time = 0  # Initialize the total waiting time
        next_available_time = 0  # Time when the chef will be free to take the next order

        for customer in customers:
            arrival_time, cooking_duration = customer
            # Calculate the time the order will be finished
            finish_time = max(arrival_time, next_available_time) + cooking_duration
            # Calculate the waiting time for the current customer
            waiting_time = finish_time - arrival_time
            # Add the waiting time to the total waiting time
            total_waiting_time += waiting_time
            # Update the next available time for the chef
            next_available_time = finish_time

        # Calculate and return the average waiting time
        return total_waiting_time / len(customers)
