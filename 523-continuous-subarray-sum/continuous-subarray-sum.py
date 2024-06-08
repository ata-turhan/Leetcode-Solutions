class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mods = {0: -1}  # Initialize with 0 at index -1 to handle edge cases
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += num
            if k != 0:
                modulus = running_sum % k
            else:
                modulus = running_sum

            # If the modulus has been seen before and the subarray is at least length 2
            if modulus in prefix_mods:
                if i - prefix_mods[modulus] > 1:
                    return True
            else:
                # Store the first occurrence of the modulus
                prefix_mods[modulus] = i

        return False
