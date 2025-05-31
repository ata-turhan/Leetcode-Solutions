from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n: int = len(board)
        
        # Helper to map a square label s (1-based) to (row, col) in Boustrophedon layout
        def get_coordinates(s: int) -> tuple[int, int]:
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            if quot % 2 == 0:
                col = rem
            else:
                col = n - 1 - rem
            return row, col
        
        # BFS queue will store (current_square, moves_taken)
        queue: deque[tuple[int, int]] = deque()
        queue.append((1, 0))
        
        visited: set[int] = set([1])
        target: int = n * n
        
        while queue:
            square, moves = queue.popleft()
            
            # Try all possible dice rolls from 1 to 6
            for nxt in range(square + 1, min(square + 6, target) + 1):
                r, c = get_coordinates(nxt)
                
                # If there's a snake/ladder at board[r][c], we must take it
                dest: int = board[r][c] if board[r][c] != -1 else nxt
                
                # If we reached the final square, return moves + 1 immediately
                if dest == target:
                    return moves + 1
                
                if dest not in visited:
                    visited.add(dest)
                    queue.append((dest, moves + 1))
        
        # If BFS completes without reaching n^2, it's unreachable
        return -1
