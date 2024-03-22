class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i] 
        #s = s.reverse()
        