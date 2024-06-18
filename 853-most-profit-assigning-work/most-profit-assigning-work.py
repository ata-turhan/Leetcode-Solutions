class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        profit_indices = [(-p, i) for i, p in enumerate(profit)]
        heapify(profit_indices)
        worker.sort()
        wi = len(worker) - 1
        total_profit = 0
        max_profit, mpi = heappop(profit_indices)
        max_profit = -max_profit
        while wi >= 0:
            if worker[wi] >= difficulty[mpi]:
                total_profit += max_profit
                wi -= 1
            else:
                if profit_indices:
                    max_profit, mpi = heappop(profit_indices)
                    max_profit = -max_profit
                else:
                    break
        return total_profit

                
        