class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()  # Initialize a set to store visited numbers
        # Iterate through the list
        for num in nums:
            if num in visited:  # If the number has been visited before, return True
                return True
            visited.add(num)  # Add the number to the set of visited numbers
        return False  # If no duplicates found, return False
