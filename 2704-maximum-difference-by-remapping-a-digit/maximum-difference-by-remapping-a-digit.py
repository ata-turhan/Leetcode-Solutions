class Solution:
    def minMaxDifference(self, num: int) -> int:
        # Convert number to string for digit manipulation
        num_str: str = str(num)

        # Generate max number by replacing the first non-9 digit with '9'
        for ch in num_str:
            if ch != '9':
                max_str: str = num_str.replace(ch, '9')
                break
        else:
            max_str = num_str  # Already all 9s

        # Generate min number by replacing the first non-0 digit with '0'
        for ch in num_str:
            if ch != '0':
                min_str: str = num_str.replace(ch, '0')
                break
        else:
            min_str = num_str  # Already all 0s

        # Return the difference between max and min
        return int(max_str) - int(min_str)
