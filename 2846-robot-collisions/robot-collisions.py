class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = [ (p, h, d) for p, h, d in zip(positions, healths, directions) ]
        robots = [ [r[0], r[1], r[2], i] for i, r in enumerate(robots)]

        stack = []
        robots.sort()


        for r in robots:
            if not stack:
                stack.append(r)
            else:
                if r[2] == "R":
                    stack.append(r)
                else:
                    if stack[-1][2] == "L":
                        stack.append(r)
                    else:
                        if stack[-1][1] == r[1]:
                            stack.pop()
                        elif stack[-1][1] > r[1]:
                            stack[-1][1] -= 1
                        else:
                            while stack and stack[-1][2] == "R" and stack[-1][1] < r[1]:
                                r[1] -= 1
                                stack.pop()
                            if not stack:
                                stack.append(r)
                            elif stack[-1][2] == "L":
                                stack.append(r)
                            elif stack[-1][1] == r[1]:
                                stack.pop()
                            elif stack[-1][1] > r[1]:
                                stack[-1][1] -= 1


        survivor_healths = [ (r[3], r[1]) for r in stack]
        survivor_healths.sort()
        return [ r[1] for r in survivor_healths]


        