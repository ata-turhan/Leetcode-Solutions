class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # Initialize with 0 to handle subarrays starting from the beginning
        total_subarrays = 0
        running_sum = 0

        for num in nums:
            running_sum += num
            remainder = running_sum % k

            if remainder in prefix_count:
                total_subarrays += prefix_count[remainder]  # Add the number of times this remainder has been seen

            prefix_count[remainder] += 1  # Increment the count of this remainder

        return total_subarrays  # Return the total number of subarrays
