class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split version strings into lists of integers
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        
        # Initialize pointers for version parts
        i, j = 0, 0
        
        # Iterate through version parts
        while i < len(v1) or j < len(v2):
            # Get the current part for each version, or 0 if no more parts
            part1 = v1[i] if i < len(v1) else 0
            part2 = v2[j] if j < len(v2) else 0
            
            # Compare the parts
            if part1 < part2:
                return -1
            elif part1 > part2:
                return 1
            else:
                # Move to the next part
                i += 1
                j += 1
                
        # Both versions are identical
        return 0
