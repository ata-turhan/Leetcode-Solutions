class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        Calculates the minimum number of operations needed to move all balls to each box.

        :param boxes: A string where '1' represents a box containing a ball and '0' represents an empty box.
        :return: A list where the ith element is the number of operations needed to move all balls to the ith box.
        """
        # Convert the string to a list of integers for easier manipulation
        boxes = list(map(int, boxes))
        
        # Initialize distances and counts for left and right movements
        left_distance, right_distance = 0, 0  # Total distance for left and right sides
        left_count, right_count = 0, 0  # Number of balls on left and right sides

        # Calculate the initial right-side distances and counts
        for idx, box in enumerate(boxes[1:], start=1):  # Start from index 1 (excluding the first box)
            if box == 1:
                right_distance += idx
                right_count += 1

        # Result array to store the number of operations for each box
        operations = [0] * len(boxes)
        # Initialize the first box's operations using right-side distances
        operations[0] = right_distance
        
        # If the first box contains a ball, update left-side distances and counts
        if boxes[0] == 1:
            left_distance += 1
            left_count += 1

        # Iterate through each box to calculate the operations required
        for i in range(1, len(boxes)):
            # Update right-side counts and distances
            if boxes[i] == 1:
                right_count -= 1
                right_distance -= 1
            right_distance -= right_count

            # Calculate operations for the current box
            operations[i] = left_distance + right_distance

            # Update left-side counts and distances
            if boxes[i] == 1:
                left_count += 1
            left_distance += left_count

        return operations
