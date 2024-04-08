class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Iterate until all students are satisfied or there's no change in the loop
        while True:
            st_len = len(students)
            for _ in range(st_len):
                # Check if the first student prefers the current sandwich
                if students[0] == sandwiches[0]:
                    students.pop(0)  # If so, remove the student from the queue
                    sandwiches.pop(0)  # Remove the served sandwich
                else:
                    students.append(students.pop(0))  # If not, move the student to the end of the queue
            # If all students are satisfied or no change in the loop, break
            if not students or len(students) == st_len:
                break 
        # Return the remaining unsatisfied students
        return len(students)
