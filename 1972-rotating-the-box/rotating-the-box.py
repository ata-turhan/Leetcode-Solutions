from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        rotated_box = [["."] * rows for _ in range(cols)]

        # Process each row to simulate gravity for stones
        for row in range(rows):
            write_pointer = cols - 1  # Pointer to place the next stone
            for col in range(cols - 1, -1, -1):
                if box[row][col] == "*":  # Obstacle
                    write_pointer = col - 1
                elif box[row][col] == "#":  # Stone
                    box[row][col] = "."
                    box[row][write_pointer] = "#"
                    write_pointer -= 1

        # Rotate the box 90 degrees clockwise
        for row in range(rows):
            for col in range(cols):
                rotated_box[col][rows - 1 - row] = box[row][col]

        return rotated_box
