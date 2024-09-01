from typing import List
import math

class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        n = len(damage)
        
        # Combine damage and health into tuples and sort them
        # Sort primarily by the effectiveness of damage per unit time (descending)
        enemies = sorted(
            [(damage[i], health[i]) for i in range(n)],
            key=lambda x: -x[0] / math.ceil(x[1] / power)  # Sort by damage per unit time to kill descending
        )
        
        total_damage = 0
        elapsed_time = 0
        
        # Calculate total damage considering the order of killing enemies
        for dmg, hp in enemies:
            time_to_kill = math.ceil(hp / power)  # Calculate the time needed to kill this enemy
            total_damage += dmg * (time_to_kill + elapsed_time)  # Accumulate the damage considering elapsed time
            elapsed_time += time_to_kill  # Increment the elapsed time after killing this enemy
        
        return total_damage
