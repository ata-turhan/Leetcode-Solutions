class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the list of people
        people.sort()
        
        # Initialize the number of boats needed
        num_boats = 0
        
        # Initialize pointers for the heaviest and lightest people
        start, end = 0, len(people) - 1
        
        # Iterate through the people
        while start <= end:
            # Check if the heaviest and lightest people can fit in one boat
            if people[start] + people[end] <= limit:
                start += 1  # Move to the next lightest person
            end -= 1  # Move to the next heaviest person
            num_boats += 1  # Increment the number of boats needed
        
        return num_boats
