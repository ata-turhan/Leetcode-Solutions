class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse():
            N = len(formula)
            stack = [defaultdict(int)]
            i = 0
            
            while i < N:
                if formula[i] == '(':
                    stack.append(defaultdict(int))
                    i += 1
                elif formula[i] == ')':
                    i += 1
                    start = i
                    while i < N and formula[i].isdigit():
                        i += 1
                    multiplicity = int(formula[start:i] or 1)
                    top = stack.pop()
                    for name, v in top.items():
                        stack[-1][name] += v * multiplicity
                else:
                    start = i
                    i += 1
                    while i < N and formula[i].islower():
                        i += 1
                    name = formula[start:i]
                    start = i
                    while i < N and formula[i].isdigit():
                        i += 1
                    multiplicity = int(formula[start:i] or 1)
                    stack[-1][name] += multiplicity
            
            return stack[0]

        count = parse()
        return ''.join(name + (str(count[name]) if count[name] > 1 else '') for name in sorted(count))


