class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens)-1
        current_power = power
        score = 0

        while l <= r:
            if current_power >= tokens[l]:
                score += 1
                current_power -= tokens[l]
                l += 1
            elif l < r and score > 0:
                score -= 1
                current_power += tokens[r]
                r -= 1
            else:
                break
                
        return score        