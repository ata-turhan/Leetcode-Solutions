class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Edge case: If there are exactly two players, return the product of their skills
        if len(skill) == 2:
            return skill[0] * skill[1]

        # Sort the skill array to facilitate pairing
        skill.sort()

        # Initialize expected_skill_sum to the sum of the first and last player's skills
        expected_skill_sum = skill[0] + skill[-1]
        # Initialize total_chemistry with the product of the first and last player's skills
        total_chemistry = skill[0] * skill[-1]

        # Loop through half of the array, pairing the ith player with the (len(skill) - i - 1)th player
        for i in range(1, len(skill) // 2):
            current_skill_sum = skill[i] + skill[-i-1]
            # If the sum of the pair's skills doesn't match the expected_skill_sum, return -1
            if current_skill_sum != expected_skill_sum:
                return -1
            # Add the product of the current pair to total_chemistry
            total_chemistry += skill[i] * skill[-i-1]

        # Return the total chemistry if all pairs had matching expected_skill_sum
        return total_chemistry
