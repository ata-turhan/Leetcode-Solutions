class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of each number in the list
        freq_counter = Counter(nums)
        
        # Convert the frequency counter to a list of tuples (number, frequency)
        freq_list = list(freq_counter.items())
        
        # Sort the list of tuples first by frequency in ascending order and then by number in descending order
        freq_list.sort(key=lambda x: (x[1], -x[0]))
        
        # Prepare the result list based on the sorted frequency list
        sorted_nums = []
        for num, freq in freq_list:
            sorted_nums.extend([num] * freq)
        
        return sorted_nums
