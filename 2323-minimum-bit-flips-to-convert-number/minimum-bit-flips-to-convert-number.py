class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Convert start and goal to their binary representations
        bin_start: str = bin(start)[2:]  # Get the binary string of start (removing '0b')
        bin_goal: str = bin(goal)[2:]    # Get the binary string of goal (removing '0b')

        # Find the maximum length between the two binary representations
        max_len: int = max(len(bin_start), len(bin_goal))

        # Pad the binary strings with leading zeros to make them the same length
        bin_start = bin_start.zfill(max_len)
        bin_goal = bin_goal.zfill(max_len)

        # Count how many bits are different between the two binary strings
        return sum(s != g for s, g in zip(bin_start, bin_goal))
