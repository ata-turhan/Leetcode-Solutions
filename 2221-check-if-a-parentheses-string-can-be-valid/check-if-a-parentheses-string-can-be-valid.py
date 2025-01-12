class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        # If length is odd, it's impossible for parentheses to be valid
        if n % 2 != 0:
            return False
        
        # minOpen: the minimum possible net "open parentheses count" so far
        # maxOpen: the maximum possible net "open parentheses count" so far
        minOpen = 0
        maxOpen = 0
        
        for i in range(n):
            if locked[i] == '1':
                # Character is fixed and cannot be changed
                if s[i] == '(':
                    minOpen += 1
                    maxOpen += 1
                else:  # s[i] == ')'
                    minOpen -= 1
                    maxOpen -= 1
            else:
                # Character is unlocked, so it can be '(' or ')'
                # Worst case: assume it's ')', so minOpen decreases
                minOpen -= 1
                # Best case: assume it's '(', so maxOpen increases
                maxOpen += 1
            
            # If maxOpen drops below 0 at any point, we have more ')' than '('
            # in every scenario, which invalidates the sequence immediately
            if maxOpen < 0:
                return False
            
            # minOpen cannot be less than 0, since we can "flip" extra ')' into '('
            if minOpen < 0:
                minOpen = 0
        
        # For the string to be valid, the minimum possible open parentheses count
        # must be zero by the end (i.e., we can balance out all opens and closes).
        return minOpen == 0
