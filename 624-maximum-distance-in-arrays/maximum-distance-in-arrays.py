class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        first_min = 10**4+1
        max_val = -10**4-1
        idx_first_min = -1
        first_max = -10**4-1

        for i, array in enumerate(arrays):
            if array[0] < first_min:
                first_min = array[0]
                max_val = array[-1]
                idx_first_min = i
            elif array[0] == first_min and array[-1] < max_val:
                max_val = array[-1]
                idx_first_min = i

        for i, array in enumerate(arrays):
            if i == idx_first_min:
                continue
            else:
                if array[-1] > first_max:
                    first_max = array[-1]

        second_min = 10**4+1
        min_val = 10**4+1
        idx_second_max = -1
        second_max = -10**4-1

        for i, array in enumerate(arrays):
            if array[-1] > second_max:
                second_max = array[-1]
                min_val = array[0]
                idx_second_max = i
            elif array[-1] == second_max and array[0] > min_val:
                min_val = array[0]
                idx_second_max = i

        for i, array in enumerate(arrays):
            if i == idx_second_max:
                continue
            else:
                if array[0] < second_min:
                    second_min = array[0]

        return max(first_max - first_min, second_max - second_min)



                

        