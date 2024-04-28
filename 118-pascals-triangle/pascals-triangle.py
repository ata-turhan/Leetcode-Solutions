class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Generate Pascal's triangle up to a given number of rows.

        Args:
        - numRows: The number of rows to generate in Pascal's triangle.

        Returns:
        - List[List[int]]: Pascal's triangle up to numRows rows.
        """
        result = []                       # Initialize an empty list to store the triangle
        prev_row = [1]                   # Start with the first row containing only 1
        result.append(prev_row)          # Append the first row to the result
        for _ in range(1, numRows):      # Iterate from the second row onwards
            new_row = [1]                # Start with 1 at the beginning of each row
            for j in range(len(prev_row) - 1):
                # Calculate the elements in between based on the previous row
                new_row.append(prev_row[j] + prev_row[j + 1])
            new_row.append(1)            # End each row with 1
            result.append(new_row)       # Append the new row to the result
            prev_row = new_row          # Update the previous row for the next iteration
        return result                    # Return the generated Pascal's triangle
