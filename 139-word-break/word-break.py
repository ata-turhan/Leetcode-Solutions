from collections import deque
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)  # Convert wordDict to a set for faster lookups
        queue = deque([0])  # Initialize queue with starting index
        seen = set()  # Set to keep track of seen indices
        
        while queue:
            start = queue.popleft()
            if start == len(s):  # If we reach the end of the string, return True
                return True
            
            for end in range(start + 1, len(s) + 1):
                if end in seen:  # Skip if end index is already seen
                    continue
                
                if s[start:end] in words:  # If substring is in wordDict
                    queue.append(end)
                    seen.add(end)  # Mark end index as seen
                
        return False  # Return False if no valid segmentation is found
