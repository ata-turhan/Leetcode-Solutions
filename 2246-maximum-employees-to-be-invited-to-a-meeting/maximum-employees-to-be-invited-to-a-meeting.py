class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        import sys
        sys.setrecursionlimit(10**7)
        from functools import lru_cache
        
        n = len(favorite)
        
        # Build reverse edges for chain calculation
        inEdges = [[] for _ in range(n)]
        for i in range(n):
            inEdges[favorite[i]].append(i)
        
        # Cycle detection data
        state = [0] * n        # 0=unvisited, 1=visiting, 2=visited
        cycle_id = [-1] * n    # ID of the cycle each node belongs to (-1 if not in a cycle)
        cycle_len = [0] * n    # Length of the cycle each node is in (0 if not in any cycle)
        
        # We'll track the order in which we visit each node to precisely locate cycles
        entry_index = [-1] * n
        dfs_stack = []
        current_cycle_id = 0
        max_cycle_size = 0
        
        def dfs(u):
            """Perform DFS to find cycles correctly, storing only the real cycle nodes."""
            nonlocal current_cycle_id, max_cycle_size
            
            state[u] = 1
            entry_index[u] = len(dfs_stack)
            dfs_stack.append(u)
            
            nxt = favorite[u]
            if state[nxt] == 0:
                dfs(nxt)
            elif state[nxt] == 1:
                # Found a cycle from nxt to current u
                # The actual cycle is everything in dfs_stack from entry_index[nxt] onward
                start_pos = entry_index[nxt]
                cycle_nodes = dfs_stack[start_pos:]  # slice of the stack that forms the cycle
                csize = len(cycle_nodes)
                max_cycle_size = max(max_cycle_size, csize)
                
                current_cycle_id += 1
                for node in cycle_nodes:
                    cycle_id[node] = current_cycle_id
                    cycle_len[node] = csize
            
            # Mark u fully visited and pop from stack
            state[u] = 2
            dfs_stack.pop()
        
        # 1) Detect cycles in each connected component
        for i in range(n):
            if state[i] == 0:
                dfs(i)
        
        # 2) Identify all 2-cycles: for nodes in a cycle of length == 2, pick the pair once
        two_cycles = []
        for i in range(n):
            if cycle_len[i] == 2:
                j = favorite[i]
                # Ensure we only record each pair once (i < j)
                if i < j and favorite[j] == i:
                    two_cycles.append((i, j))
        
        # 3) For chain expansions, define a function that returns
        #    the longest chain ending at `node`, ignoring the edge from `ignore -> node`.
        @lru_cache(None)
        def get_chain_length(node, ignore):
            # If node belongs to a cycle of length >= 3, it can't be used for chain expansions
            # that attach onto a 2-cycle pair.
            if cycle_len[node] >= 3:
                return 0
            
            best = 0
            for p in inEdges[node]:
                if p == ignore:
                    continue
                best = max(best, 1 + get_chain_length(p, ignore))
            return best
        
        # 4) Sum expansions for all 2-cycles
        sum_2_cycle_chains = 0
        for (u, v) in two_cycles:
            cu = get_chain_length(u, v)
            cv = get_chain_length(v, u)
            sum_2_cycle_chains += (cu + cv + 2)
        
        # 5) Final result: either we seat one cycle of length >=3, or
        #    we seat all disjoint 2-cycles with their chain expansions.
        return max(max_cycle_size, sum_2_cycle_chains)
