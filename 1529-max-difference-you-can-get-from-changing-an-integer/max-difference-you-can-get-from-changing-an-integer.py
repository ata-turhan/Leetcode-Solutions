class Solution:
    def maxDiff(self, num: int) -> int:
        num_str: str = str(num)

        # Generate maximum possible value by replacing the first non-9 digit with 9
        for digit in num_str:
            if digit != '9':
                max_num = int(num_str.replace(digit, '9'))
                break
        else:
            max_num = num  # Already all 9s

        # Generate minimum possible value
        if num_str[0] != '1':
            min_num = int(num_str.replace(num_str[0], '1'))
        else:
            # Replace the first digit (not 0 or 1) that is not the first digit
            for i in range(1, len(num_str)):
                if num_str[i] not in ['0', '1']:
                    min_num = int(num_str.replace(num_str[i], '0'))
                    break
            else:
                min_num = num  # All digits are 1 or 0, can't minimize more

        return max_num - min_num
