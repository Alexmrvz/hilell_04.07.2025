from typing import Optional

class Human:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        self.gender: str = gender
        self.age: int = age
        self.first_name: str = first_name
        self.last_name: str = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} y.o."


class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book: str = record_book

    def __str__(self) -> str:
        return (f"Student: {self.first_name} {self.last_name}, "
                f"{self.gender}, {self.age} y.o., record book: {self.record_book}")


class Group:
    def __init__(self, number: str) -> None:
        self.number: str = number
        self.group: list[Student] = []

    def add_student(self, student: Student) -> None:
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
        all_students: str = "\n".join(str(student) for student in self.group)
        return f"Group number: {self.number}\n{all_students}"


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
