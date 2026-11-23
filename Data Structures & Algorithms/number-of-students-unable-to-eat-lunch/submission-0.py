class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        count = 0
        while students:
            front = students.popleft()
            top = sandwiches[0]

            if front == top:
                sandwiches.popleft()
                count = 0
            else:
                students.append(front)
                count += 1

            if count == len(students):
                break

        return len(students)