class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Sort the intervals by start time
        intervals.sort(key=lambda interval: interval[0])
        
        # Min heap to keep track of the end times of the meetings currently using a room
        heap = []
        
        for interval in intervals:
            # If the earliest meeting in the heap is finished before the new meeting starts
            if heap and heap[0] <= interval[0]:
                heapq.heappop(heap)  # Remove it from the heap
            
            # Add the new meeting's end time to the heap
            heapq.heappush(heap, interval[1])
        
        # The size of the heap is the number of rooms required
        return len(heap)
