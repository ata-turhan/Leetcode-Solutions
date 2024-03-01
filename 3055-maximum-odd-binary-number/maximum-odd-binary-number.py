class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        arr = list(s)
        arr[0:ones-1] = ["1"] * (ones-1)
        arr[ones-1:-1] = ["0"] * (len(arr)-ones)
        arr[-1] = "1"
        return "".join(arr)
        