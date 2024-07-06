class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # Function to determine the maximum height when starting with the given color
        def max_height(start_with_red: bool) -> int:
            red_count = 0
            blue_count = 0
            use_red = start_with_red
            height = 0

            for i in range(1, max(red, blue) + 1):
                if use_red:
                    red_count += i
                    if red_count > red:
                        break
                    else:
                        height = max(height, i)
                else:
                    blue_count += i
                    if blue_count > blue:
                        break
                    else:
                        height = max(height, i)
                use_red = not use_red

            return height

        # Calculate the maximum height starting with red and blue respectively
        max_height_starting_red = max_height(True)
        max_height_starting_blue = max_height(False)

        # Return the maximum of the two heights
        return max(max_height_starting_red, max_height_starting_blue)
