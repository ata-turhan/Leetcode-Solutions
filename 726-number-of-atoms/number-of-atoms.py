class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse():
            N = len(formula)
            stack = [defaultdict(int)]  # Stack to keep track of counts in nested parentheses
            i = 0  # Pointer to traverse the formula
            
            while i < N:
                if formula[i] == '(':
                    stack.append(defaultdict(int))  # Start a new scope for the nested formula
                    i += 1
                elif formula[i] == ')':
                    i += 1
                    start = i
                    while i < N and formula[i].isdigit():
                        i += 1
                    multiplicity = int(formula[start:i] or 1)  # Multiplier for the nested formula
                    top_counts = stack.pop()  # Pop the counts from the nested scope
                    for element, count in top_counts.items():
                        stack[-1][element] += count * multiplicity  # Multiply and add to the previous scope
                else:
                    start = i
                    i += 1
                    while i < N and formula[i].islower():
                        i += 1
                    element = formula[start:i]  # Extract the element name
                    start = i
                    while i < N and formula[i].isdigit():
                        i += 1
                    multiplicity = int(formula[start:i] or 1)  # Get the count of the element
                    stack[-1][element] += multiplicity  # Add the count to the current scope
            
            return stack[0]

        element_counts = parse()
        # Construct the result string by sorting the elements and appending their counts
        return ''.join(element + (str(element_counts[element]) if element_counts[element] > 1 else '') for element in sorted(element_counts))
