from typing import Optional
from student import Student

class GroupLimitError(Exception):
    def __init__(self, message: str = "Group already has 10 students!") -> None:
        super().__init__(message)

class Group:
    def __init__(self, number: str) -> None:
        self.number = number
        self.group: list[Student] = []

    def add_student(self, student: Student) -> None:
        if len(self.group) >= 10:
            raise GroupLimitError(
                f"Cannot add {student.first_name} {student.last_name}: group already has 10 students!"
            )
        for s in self.group:
            if s.last_name == student.last_name and s.record_book == student.record_book:
                return
        self.group.append(student)

    def delete_student(self, last_name: str) -> None:
        student: Optional[Student] = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name: str) -> Optional[Student]:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self) -> str:
        all_students = "\n".join(str(student) for student in self.group)
        return f"Group number: {self.number} (students: {len(self.group)})\n{all_students}"