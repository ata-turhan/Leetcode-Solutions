from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # If source and target are the same, no buses are needed
        if source == target:
            return 0

        # Map to keep track of buses (by index) accessible from each stop
        stop_to_buses = defaultdict(set)
        for bus_index, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].add(bus_index)

        # Initialize BFS
        steps = 0
        visited_buses = set()
        queue = deque([source])

        # BFS traversal
        while queue:
            level_size = len(queue)
            steps += 1

            for _ in range(level_size):
                current_stop = queue.popleft()

                # Check if we reached the target
                if current_stop == target:
                    return steps - 1

                # Add all stops accessible by unvisited buses from the current stop
                for bus_index in stop_to_buses[current_stop]:
                    if bus_index not in visited_buses:
                        visited_buses.add(bus_index)
                        queue.extend(routes[bus_index])

        return -1
