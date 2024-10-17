class Solution:
    def maximumSwap(self, num: int) -> int:
        num_arr = list(map(int, str(num)))
        max_val = -1
        max_idx = -1 
        for i in range(len(num_arr)-1):
            for j in range(i+1, len(num_arr)):
                if num_arr[j] > num_arr[i] and num_arr[j] >= max_val:
                    max_val = num_arr[j]
                    max_idx = j
            if max_val != -1:
                num_arr[i], num_arr[max_idx] = num_arr[max_idx], num_arr[i]
                return int("".join(map(str, num_arr)))
        return num
                    

        