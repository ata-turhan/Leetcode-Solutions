class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # dp[i] for questions i to n-1, with dp[n] = 0 as base case
        
        # Process questions in reverse order
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            # Calculate the index of the next question that can be attempted after solving the current one
            next_index = i + brainpower + 1
            
            # Option 1: Solve the current question
            solve = points + (dp[next_index] if next_index < n else 0)
            # Option 2: Skip the current question
            skip = dp[i + 1]
            
            # Take the maximum of the two choices
            dp[i] = max(solve, skip)
        
        return dp[0]
