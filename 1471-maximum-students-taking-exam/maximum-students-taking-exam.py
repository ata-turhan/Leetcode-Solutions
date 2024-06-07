from typing import List

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        def count_bits(x):
            """
            Count the number of 1s in the binary representation of x.
            
            :param x: Integer to count bits.
            :return: Number of 1s in binary representation of x.
            """
            count = 0
            while x:
                x &= x - 1
                count += 1
            return count

        m, n = len(seats), len(seats[0])
        # dp[row][state] represents the maximum number of students that can be seated
        # up to row `row` with the seat configuration `state`
        dp = [[0] * (1 << n) for _ in range(m + 1)]
        
        for row in range(1, m + 1):
            cur_seat = 0
            # Encode the current row's seat availability in a bitmask
            for col in range(n):
                if seats[row - 1][col] == '.':
                    cur_seat |= (1 << col)
            # Iterate over all possible seat configurations for the current row
            for cur_mask in range(1 << n):
                # Check if the current mask is a valid configuration
                if (cur_mask & cur_seat) == cur_mask and not (cur_mask & (cur_mask >> 1)):
                    # Iterate over all possible seat configurations for the previous row
                    for prev_mask in range(1 << n):
                        # Check if the previous mask is a valid configuration and compatible with the current mask
                        if (prev_mask & (prev_mask >> 1)) == 0 and \
                           (prev_mask & (cur_mask >> 1)) == 0 and \
                           (prev_mask & (cur_mask << 1)) == 0:
                            # Update dp[row][cur_mask] with the maximum number of students
                            dp[row][cur_mask] = max(dp[row][cur_mask], 
                                                    dp[row - 1][prev_mask] + count_bits(cur_mask))

        # The maximum number of students is the maximum value in the last row of dp
        return max(dp[m])