class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        available_seats = list(range(n))
        seated_friends = []
        times_with_idx = [(arrival, leave, i) for i, (arrival, leave) in enumerate(times)]
        times_with_idx.sort()
        for i in range(n):
            arrival, leave, friend_idx = times_with_idx[i]
            while seated_friends and seated_friends[0][0] <= arrival:
                _, seat_to_empty = heappop(seated_friends)
                heappush(available_seats, seat_to_empty)
            available_seat = heappop(available_seats)
            heappush(seated_friends, (leave, available_seat))
            if friend_idx == targetFriend:
                return available_seat
        