from collections import defaultdict
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build the invocation graph and reverse graph (invoker -> invoked)
        invocation_graph = defaultdict(list)  # Regular graph: a -> b (a invokes b)
        reverse_invocation_graph = defaultdict(list)  # Reverse graph: b -> a (b invoked by a)
        
        for invoker, invoked in invocations:
            invocation_graph[invoker].append(invoked)
            reverse_invocation_graph[invoked].append(invoker)
        
        # Step 2: Use DFS to find all suspicious methods starting from method k
        suspicious_methods = set()  # Set to store all suspicious methods
        stack = [k]
        
        while stack:
            current_method = stack.pop()
            if current_method not in suspicious_methods:
                suspicious_methods.add(current_method)
                for neighbor in invocation_graph[current_method]:
                    if neighbor not in suspicious_methods:
                        stack.append(neighbor)
        
        # Step 3: Check for external invocations (non-suspicious methods invoking suspicious ones)
        for method in suspicious_methods:
            for invoker in reverse_invocation_graph[method]:
                if invoker not in suspicious_methods:
                    # If a non-suspicious method invokes a suspicious method, return all methods
                    return list(range(n))
        
        # Step 4: Return all non-suspicious methods
        remaining_methods = [i for i in range(n) if i not in suspicious_methods]
        
        return remaining_methods
