class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        Compute the final state of dominoes after all pushes resolve.
        We simulate net forces from 'R' and 'L' pushes in two linear passes.
        """
        n: int = len(dominoes)
        # forces[i] will hold net force: +ve for rightward, -ve for leftward
        forces: list[int] = [0] * n

        # --- Left to right: accumulate rightward forces ---
        force: int = 0
        for i, ch in enumerate(dominoes):
            if ch == 'R':
                force = n            # maximal rightward force
            elif ch == 'L':
                force = 0            # cancel any rightward force
            else:
                force = max(force - 1, 0)
            forces[i] += force

        # --- Right to left: accumulate leftward forces (subtract) ---
        force = 0
        for i in range(n - 1, -1, -1):
            ch: str = dominoes[i]
            if ch == 'L':
                force = n            # maximal leftward force
            elif ch == 'R':
                force = 0            # cancel any leftward force
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        # --- Build the resulting string based on net forces ---
        result_chars: list[str] = []
        for net_force in forces:
            if net_force > 0:
                result_chars.append('R')
            elif net_force < 0:
                result_chars.append('L')
            else:
                result_chars.append('.')

        return ''.join(result_chars)
