class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num_counts = Counter(nums)  # Count occurrences of each number
        unique_nums = sorted(num_counts.keys())  # Get sorted unique numbers
        max_points = [0] * (len(unique_nums) + 1)  # Initialize dp array
        max_points[1] = num_counts[unique_nums[0]] * unique_nums[0]  # Base case for first number

        for i, num in enumerate(unique_nums[1:], start=2):
            if num - 1 == unique_nums[i - 2]:  # If current number is consecutive to previous
                max_points[i] = max(max_points[i - 1], num_counts[num] * num + max_points[i - 2])
            else:
                max_points[i] = max_points[i - 1] + num_counts[num] * num  # If not consecutive

        return max_points[-1]  # Maximum points that can be earned
