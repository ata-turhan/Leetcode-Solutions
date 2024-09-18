class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        lst = []

        for ele in nums:
            lst += [str(ele)]
        
        n = len(lst)

        for i in range(n):
            for j in range(i+1 , n):
                
                if str(lst[i]) + str(lst[j]) > str(lst[j]) + str(lst[i]):
                    # if current order is greatest value .. continue
                    continue
                else:
                    # else swap the values ..!!!
                    lst[i] , lst[j] = lst[j] , lst[i]
        
        
        ans = ''.join(lst)

        if int(ans) == 0:
            return "0"
        
        return ans
        