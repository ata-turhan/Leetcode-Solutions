from collections import deque
from typing import List

class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int]
    ) -> int:
        """
        Use a BFS‐like approach to repeatedly open boxes that we both have and are openable.
        Once we open a box i, we:
          1) collect candies[i],
          2) mark all keys[i] as obtained → if any of those boxes are already in possession, enqueue them,
          3) mark all containedBoxes[i] as now in possession → if they are openable, enqueue them.
        
        Return the total number of candies collected.
        """
        n: int = len(status)

        # Track which boxes we physically have
        have: List[bool] = [False] * n
        # Track which box‐keys we have collected
        haveKey: List[bool] = [False] * n
        # Track which boxes we've already opened (visited)
        visited: List[bool] = [False] * n

        queue: deque[int] = deque()
        total_candies: int = 0

        # 1) Mark initial boxes as "in possession". If any are already open, add to queue.
        for b in initialBoxes:
            have[b] = True
            if status[b] == 1:
                queue.append(b)

        # 2) Process until no more openable boxes remain
        while queue:
            box_index = queue.popleft()

            # If we've already processed this box, skip
            if visited[box_index]:
                continue

            # Mark as opened (visited), collect candies
            visited[box_index] = True
            total_candies += candies[box_index]

            # 2a) Acquire any new keys from this box
            for k in keys[box_index]:
                if not haveKey[k]:
                    haveKey[k] = True
                    # If we already have box k physically and haven't opened it yet, enqueue it
                    if have[k] and not visited[k]:
                        queue.append(k)

            # 2b) Acquire any new contained boxes from this box
            for inner in containedBoxes[box_index]:
                if not have[inner]:
                    have[inner] = True
                    # If that box is already openable (status == 1 or we hold its key), enqueue it
                    if (status[inner] == 1 or haveKey[inner]) and not visited[inner]:
                        queue.append(inner)

        return total_candies
