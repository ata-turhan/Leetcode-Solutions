from typing import List
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        # Step 1: Find the maximum value in the array to set the size of the counting array
        max_value = max(nums)
        n = len(nums)
        
        # Step 2: Count the occurrences of each number in nums
        count_nums = [0] * (max_value + 1)
        for num in nums:
            count_nums[num] += 1

        # Step 3: Count how many multiples of g exist in nums for each g (divisor counting)
        divisor_counts = [0] * (max_value + 1)
        for g in range(1, max_value + 1):
            for multiple in range(g, max_value + 1, g):
                divisor_counts[g] += count_nums[multiple]

        # Step 4: Calculate the number of pairs with gcd = g
        gcd_pairs = [0] * (max_value + 1)
        for g in range(max_value, 0, -1):
            total_pairs_with_g = divisor_counts[g] * (divisor_counts[g] - 1) // 2
            gcd_pairs[g] = total_pairs_with_g
            # Subtract pairs that belong to multiples of g
            for multiple in range(2 * g, max_value + 1, g):
                gcd_pairs[g] -= gcd_pairs[multiple]

        # Step 5: Collect gcd values with positive pairs and build cumulative positions
        gcd_with_pairs = []
        for g in range(1, max_value + 1):
            if gcd_pairs[g] > 0:
                gcd_with_pairs.append((g, gcd_pairs[g]))

        # Step 6: Build the cumulative positions for binary search
        positions = [0]
        for g, count in gcd_with_pairs:
            positions.append(positions[-1] + count)

        # Step 7: Process the queries using binary search on the positions
        total_pairs = positions[-1]
        result = []
        for q in queries:
            index = bisect.bisect_right(positions, q) - 1
            result.append(gcd_with_pairs[index][0])

        return result
