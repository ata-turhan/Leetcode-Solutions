class Solution:
    def punishmentNumber(self, n: int) -> int:
        """
        Calculates the punishment number by checking if each squared number 
        can be partitioned into segments summing up to the original number.
        """

        def can_partition_to_sum(square_str: str, target_sum: int) -> bool:
            """
            Determines if the squared number (as a string) can be partitioned 
            into consecutive parts that sum up to target_sum.
            """

            def dfs(index: int, current_sum: int, current_part: str) -> bool:
                """
                Recursively checks different partition possibilities.
                - index: Current position in the square_str
                - current_sum: Sum accumulated so far
                - current_part: Current number segment being formed
                """
                if index == len(square_str):
                    return current_sum + int(current_part) == target_sum
                if current_sum > target_sum:
                    return False

                # Try continuing the current partition OR finishing it and starting a new partition
                return (
                    dfs(index + 1, current_sum, current_part + square_str[index])
                    or dfs(index + 1, current_sum + int(current_part), square_str[index])
                )

            return dfs(0, 0, "0")

        total_punishment = 0

        for num in range(1, n + 1):
            squared_str = str(num * num)
            if can_partition_to_sum(squared_str, num):
                total_punishment += num * num

        return total_punishment
