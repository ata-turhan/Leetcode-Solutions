class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = list(map(int, list(boxes)))
        left_dist, right_dist = 0, 0
        left_ones, right_ones = 0, 0

        for i, box in enumerate(boxes[1:], start=1):
            if box == 1:
                right_dist += i
                right_ones += 1 

        res = [0] * len(boxes)
        res[0] = right_dist
        if boxes[0] == 1:
            left_dist += 1
            left_ones += 1


        for i in range(1, len(boxes)):
            if boxes[i] == 1:
                right_ones -= 1
                right_dist -= 1

            right_dist -= right_ones

            res[i] = left_dist + right_dist

            if boxes[i] == 1:
                left_ones += 1

            left_dist += left_ones

        return res




            
