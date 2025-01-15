class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bin_num1 = bin(num1)[2:]
        bin_num2 = bin(num2)[2:]

        count_set_bits = bin_num2.count("1")

        x = [0] * len(bin_num1)

        for i in range(len(bin_num1)):
            if bin_num1[i] == "1":
                x[i] = 1
                count_set_bits -= 1

            if count_set_bits == 0:
                break

        if count_set_bits != 0:
            for i in range(len(bin_num1) - 1, -1, -1):
                if bin_num1[i] == "0":
                    x[i] = 1
                    count_set_bits -= 1

                if count_set_bits == 0:
                    break

            if count_set_bits != 0:
                x = [1] * count_set_bits + x

        return int("".join(map(str, x)), 2)

        