class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        non_distinct_counts = sum(val > 1 for val in counter.values())
        num_operations = 0
        nums.reverse()

        while non_distinct_counts > 0:
            if len(nums) <= 3:
                num_operations += 1
                break
            else:
                for _ in range(3):
                    removed_val = nums.pop()
                    counter[removed_val] -= 1
                    if counter[removed_val] == 1:                 
                        non_distinct_counts -= 1
                num_operations += 1

        return num_operations
        