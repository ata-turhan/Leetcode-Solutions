class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2:
            return skill[0] * skill[-1]

        skill.sort()
        total_skill = skill[0] + skill[-1]
        total_cem = skill[0] * skill[-1]
        for i in range(1, len(skill)//2):
            new_total_skill = skill[i] + skill[-i-1]
            if new_total_skill != total_skill:
                return -1
            else:
                total_cem += skill[i] * skill[-i-1]

        return total_cem
        