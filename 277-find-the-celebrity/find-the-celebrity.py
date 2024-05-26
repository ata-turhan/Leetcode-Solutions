# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        Finds the celebrity in a party of n people. A celebrity is defined as someone who:
        - Is known by everyone.
        - Does not know anyone.
        
        :param n: int - The number of people at the party.
        :return: int - The index of the celebrity or -1 if there is no celebrity.
        """
        # Initial candidate for celebrity is person 0.
        candidate = 0
        
        # Determine the potential celebrity.
        for i in range(1, n):
            # If candidate knows i, then candidate cannot be a celebrity, update candidate to i.
            if knows(candidate, i):
                candidate = i
        
        # Verify that the candidate is a true celebrity.
        for i in range(n):
            # Skip the candidate itself.
            if i == candidate:
                continue
            # Candidate must not know anyone and everyone must know the candidate.
            if knows(candidate, i) or not knows(i, candidate):
                return -1
        
        return candidate

# Example usage:
# sol = Solution()
# print(sol.findCelebrity(4))  # Replace 4 with the actual number of people at the party
