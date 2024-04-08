class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while True:
            st_len = len(students)
            for _ in range(st_len):
                if students[0] == sandwiches[0]:
                    students.pop(0)
                    sandwiches.pop(0)
                else:
                    students.append(students.pop(0))
            if not students or len(students) == st_len:
                break 
        return len(students)