from collections import defaultdict

class TwoSum:
    def __init__(self):
        # Initialize a dictionary to store the count of each number
        self.nums = defaultdict(int)

    def add(self, number: int) -> None:
        # Increment the count of the number in the dictionary
        self.nums[number] += 1

    def find(self, value: int) -> bool:
        # Convert the keys of the dictionary to a list
        arr = list(self.nums.keys())
        
        # Iterate through the numbers in the list
        for num in arr:
            # Calculate the complement of the current number
            complement = value - num
            
            # Check if the complement exists in the dictionary
            if complement in self.nums:
                # If the complement is the same as the current number, 
                # ensure there are at least two occurrences of the number in the dictionary
                if num == complement and self.nums[complement] == 1:
                    continue
                else:
                    return True
        
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
