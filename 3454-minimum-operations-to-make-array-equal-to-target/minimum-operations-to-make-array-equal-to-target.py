class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        array = [0] * len(nums)

        for i in range(len(target)):
            array[i] = target[i] - nums[i]
        
        operations = 0
        prev = 0
        negative = True if array[0] < 0 else False
        print(array)
        
        for i in range(len(array)):
            cur = array[i]
            if negative:
                operations += max(0, prev - cur)
                if i < len(array)-1 and array[i+1] >= 0:
                    negative = False
                    prev = 0
                else:
                    prev = cur
            else:
                operations += max(0, cur - prev)
                if i < len(array)-1 and array[i+1] < 0:
                    negative = True
                    prev = 0
                else:
                    prev = cur
            print(cur, operations)

        return operations