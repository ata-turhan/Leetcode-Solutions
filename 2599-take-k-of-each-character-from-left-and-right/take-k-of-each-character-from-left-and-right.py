class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        counter = Counter(s)
        if counter["a"] < k or counter["b"] < k or counter["c"] < k:
            return -1
        
        right = len(s)
        window = defaultdict(int)
        required_count = 0
        while required_count < 3:
            right -= 1
            window[s[right]] += 1
            if window[s[right]] == k:
                required_count += 1

        min_char = len(s) - right          

        for left in range(len(s)):
            window[s[left]] += 1

            while right < len(s) and window[s[right]] != k:       
                window[s[right]] -= 1
                right += 1

            if left < right:
                min_char = min(min_char, left + 1 + len(s) - right)

        return min_char
            

        