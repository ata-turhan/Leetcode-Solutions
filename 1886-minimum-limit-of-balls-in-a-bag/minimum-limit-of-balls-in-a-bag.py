class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        """
        Finds the minimum possible size of the largest bag after performing up to maxOperations splits.
        
        :param nums: List of integers representing the sizes of the bags.
        :param maxOperations: Maximum number of allowed operations to split bags.
        :return: The minimum possible size of the largest bag.
        """

        def calc_operations(arr: List[int], max_size: int) -> int:
            """
            Calculates the total number of splits required to ensure all bag sizes
            are <= max_size.

            :param arr: List of integers representing bag sizes.
            :param max_size: The target maximum size for any bag.
            :return: The total number of operations needed.
            """
            operations = 0
            for size in arr:
                # Calculate how many splits are needed for this bag
                operations += math.ceil(size / max_size) - 1
            return operations

        # Binary search boundaries
        left, right = 1, max(nums)
        result = 0

        while left <= right:
            mid = (left + right) // 2  # Midpoint as a candidate for the maximum bag size
            required_operations = calc_operations(nums, mid)
            
            if required_operations <= maxOperations:
                # If the current max_size can be achieved within maxOperations, try smaller sizes
                result = mid
                right = mid - 1
            else:
                # Otherwise, increase the candidate max_size
                left = mid + 1

        return result
