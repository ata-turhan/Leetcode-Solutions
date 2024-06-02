import heapq
from typing import List

class Solution:
    def clearStars(self, s: str) -> str:
        """
        Removes characters from the string 's' that are followed by a '*' character.
        
        :param s: str - The input string containing characters and '*'.
        :return: str - The resulting string after removing characters followed by '*'.
        """
        heap = []  # Initialize a heap to store characters and their indices
        deleted = set()  # Initialize a set to store indices of characters to be deleted

        # Iterate over the characters in the string
        for i, c in enumerate(s):
            if c == "*":  # If the current character is '*'
                deleted.add(i)  # Add the index of '*' to the deleted set
                if heap:  # If the heap is not empty
                    char, idx = heapq.heappop(heap)  # Pop the last character from the heap
                    deleted.add(-idx)  # Add the index of the character to the deleted set
            else:
                heapq.heappush(heap, (c, -i))  # Push the character and its index to the heap

        res = []  # Initialize the result list to store the final characters
        # Iterate over the characters in the string again
        for i, c in enumerate(s):
            if i not in deleted:  # If the index is not in the deleted set
                res.append(c)  # Add the character to the result list

        return "".join(res)  # Join the result list into a string and return

# Example usage:
# sol = Solution()
# print(sol.clearStars("ab*c*d"))  # Output: "acd"
# print(sol.clearStars("a*b*c*"))  # Output: ""
# print(sol.clearStars("a*bc*d"))  # Output: "cd"
