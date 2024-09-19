class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Parse the expression into tokens
        tokens = self.parseExpression(expression)
        memo = {}
        
        # Recursive function with memoization
        def dfs(start, end):
            # Check if result is already computed
            if (start, end) in memo:
                return memo[(start, end)]
            
            # If the sub-expression is a single number
            if start == end:
                return [tokens[start]]
            
            results = []
            # Iterate over the tokens to find operators
            for i in range(start + 1, end, 2):
                op = tokens[i]
                # Recursively compute left and right sub-expressions
                left_results = dfs(start, i - 1)
                right_results = dfs(i + 1, end)
                
                # Combine the results from left and right sub-expressions
                for left in left_results:
                    for right in right_results:
                        results.append(self.compute(left, right, op))
            
            # Store the computed results in memo
            memo[(start, end)] = results
            return results
        
        # Start the recursion from the full expression
        return dfs(0, len(tokens) - 1)
    
    def parseExpression(self, expression):
        tokens = []
        num = 0
        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                num = 0
                while i < len(expression) and expression[i].isdigit():
                    num = num * 10 + int(expression[i])
                    i += 1
                tokens.append(num)
            else:
                tokens.append(expression[i])
                i += 1
        return tokens

    def compute(self, left, right, op):
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        else:  # op == '*'
            return left * right
