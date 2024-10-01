class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr = [num % k for num in arr]
        zero_count = arr.count(0)
        if zero_count % 2 == 1:
            return False
        arr_no_zeros = [num for num in arr if num != 0]
        arr_no_zeros.sort()
        l = 0
        r = len(arr_no_zeros) - 1
        while l < r:
            if (arr_no_zeros[l] + arr_no_zeros[r]) == k:
                l += 1
                r -= 1
            else:
                return False
        return True
        