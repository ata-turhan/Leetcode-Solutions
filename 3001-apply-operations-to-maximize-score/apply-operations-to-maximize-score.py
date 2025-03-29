class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        
        # Step 1: Precompute smallest prime factors (SPF) for numbers up to max(nums)
        max_val = max(nums)
        spf = [0] * (max_val + 1)
        for i in range(2, max_val + 1):
            if spf[i] == 0:  # i is prime
                for j in range(i, max_val + 1, i):
                    if spf[j] == 0:
                        spf[j] = i
        
        # Function to compute the prime score (number of distinct prime factors)
        def prime_score(x: int) -> int:
            cnt = 0
            prev = -1
            while x > 1:
                p = spf[x]
                if p != prev:
                    cnt += 1
                    prev = p
                x //= p
            return cnt
        
        # Compute prime score for each number in nums
        s = [prime_score(x) for x in nums]
        
        # Step 2: Use monotonic stacks to compute left and right boundaries for each index.
        left = [-1] * n
        stack = []
        for i in range(n):
            # We need the nearest index with prime score >= s[i]
            while stack and s[stack[-1]] < s[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            # We need the nearest index with prime score > s[i]
            while stack and s[stack[-1]] <= s[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        # Frequency: number of subarrays where nums[i] is the chosen element
        freq = [(i - left[i]) * (right[i] - i) for i in range(n)]
        
        # Step 3: Prepare the (value, frequency) pairs and sort in descending order by value.
        pairs = [(nums[i], freq[i]) for i in range(n)]
        pairs.sort(key=lambda x: x[0], reverse=True)
        
        # Greedily use operations for the highest multipliers first.
        ans = 1
        remaining = k
        for value, count in pairs:
            if remaining <= 0:
                break
            use = min(count, remaining)
            ans = ans * pow(value, use, mod) % mod
            remaining -= use
        
        return ans
