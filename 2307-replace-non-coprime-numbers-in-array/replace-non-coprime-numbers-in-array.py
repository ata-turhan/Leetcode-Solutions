from typing import List
from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        """
        Algorithm (Monotonic Stack by GCD/LCM merging):
        - Keep a stack `st` of already-processed values.
        - For each number `a` in nums, repeatedly merge it with the stack top while
          the GCD(top, a) > 1. Replace the pair by LCM(top, a) and continue trying
          to merge the new value leftward (with the new top), until the GCD becomes 1
          or the stack is empty.
        - Push the final value back to the stack.
        - The process is equivalent to repeatedly merging any adjacent non-coprime pair,
          and (as per problem statement) order of merges does not affect the final result.
        
        Correctness intuition:
        - When two adjacent numbers share a factor (>1), replacing them by their LCM preserves
          divisibility relations with neighbors. If the new LCM shares a factor with the value
          immediately to its left, it must be merged as well; the while-loop enforces this
          until the boundary is coprime or the stack is empty.
        - Associativity here relies on the fact that gcd/lcm propagate common prime factors:
          merging leftwards until coprime is equivalent to any sequence of adjacent merges.
        
        Complexity:
        - Each element is pushed once and popped at most once ⇒ amortized O(n) merges.
        - Each gcd call is O(log A) where A ≤ 1e5 for inputs and final values ≤ 1e8.
        - Total time: O(n log A). Space: O(n) for the stack.
        """
        st: List[int] = []

        for a in nums:
            x = a
            # Merge leftward while the top shares a common factor with x
            while st:
                g = gcd(st[-1], x)
                if g == 1:
                    break
                # LCM without overflow: lcm(u, v) = u / gcd(u, v) * v
                x = (st[-1] // g) * x
                st.pop()
            st.append(x)

        return st
