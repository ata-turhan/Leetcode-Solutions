class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair_cars_in_t_time(ranks, cars, t):
            repaired_cars = 0

            for rank in ranks:
                repaired_cars += int(math.sqrt(t / rank))
                if repaired_cars >= cars:
                    return True

            return False

        left, right = 1, max(ranks) * cars**2
        min_time = float("inf")

        while left <= right:
            mid = left + (right - left) // 2
            if can_repair_cars_in_t_time(ranks, cars, mid):
                min_time = mid
                right = mid - 1
            else:
                left = mid + 1

        return min_time
        