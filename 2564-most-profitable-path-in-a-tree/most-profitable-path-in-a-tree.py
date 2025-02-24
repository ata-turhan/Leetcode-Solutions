from math import inf
from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:        
        # Build the undirected tree.
        graph = defaultdict(list)
        n = len(amount)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize an array to record Bob's arrival times for nodes along his unique path from bob to node 0.
        bobTime = [inf] * n
        
        # DFS to compute Bob's path from his starting node to the root.
        # When a node is on Bob's path, record the time (distance from bob).
        def dfsBob(cur: int, parent: int, t: int) -> bool:
            # If we've reached node 0, record and return success.
            if cur == 0:
                bobTime[cur] = t
                return True
            for nxt in graph[cur]:
                if nxt == parent:
                    continue
                if dfsBob(nxt, cur, t + 1):
                    bobTime[cur] = t
                    return True
            return False
        
        dfsBob(bob, -1, 0)
        
        # Now, perform DFS for Alice starting from node 0.
        # At each node, update her net profit based on who reached the gate first.
        ans = -inf
        
        def dfsAlice(cur: int, parent: int, t: int, profit: int):
            nonlocal ans
            # Determine the income effect at the current node.
            if t < bobTime[cur]:
                curProfit = profit + amount[cur]
            elif t == bobTime[cur]:
                curProfit = profit + (amount[cur] // 2)
            else:
                curProfit = profit  # Bob reached earlier, so no change.
            
            # If it's a leaf node (and not the root with no children), update the answer.
            if cur != 0 and len(graph[cur]) == 1:
                ans = max(ans, curProfit)
                return
            
            # Continue DFS to adjacent nodes.
            for nxt in graph[cur]:
                if nxt == parent:
                    continue
                dfsAlice(nxt, cur, t + 1, curProfit)
        
        dfsAlice(0, -1, 0, 0)
        return ans
