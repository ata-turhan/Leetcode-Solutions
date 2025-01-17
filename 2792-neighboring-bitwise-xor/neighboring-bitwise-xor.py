class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        original = [1]
        
        for i in range(len(derived) - 1):
            if derived[i] == 1:
                original.append(1 - original[-1])
            else:
                original.append(original[-1])

        return (original[0] ^ original[-1]) == derived[-1]

        