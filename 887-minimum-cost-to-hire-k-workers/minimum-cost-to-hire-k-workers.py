class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        total_cost = float("inf")
        qualities = []
        wages_to_qualities = list(sorted((w/q, q) for w, q in zip(wage, quality) ))
        cur_total_quantity = 0

        for i in range(len(wages_to_qualities)):
            heapq.heappush(qualities, -wages_to_qualities[i][1])
            cur_total_quantity += wages_to_qualities[i][1]

            if len(qualities) > k:
                cur_max_quantity = -heapq.heappop(qualities)
                cur_total_quantity -= cur_max_quantity

            if len(qualities) == k:
                cur_max_wage_to_quality = wages_to_qualities[i][0]
                total_cost = min(total_cost, cur_total_quantity * cur_max_wage_to_quality)

        return total_cost
