from student import Student
from group import Group, GroupLimitError


def run_demo():
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

    gr = Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)
    print(gr)

    assert gr.find_student('Jobs') == st1
    assert gr.find_student('Jobs2') is None

    gr.delete_student('Taylor')
    print("\nAfter deleting Taylor:")
    print(gr)

    try:
        for i in range(3, 13):
            gr.add_student(Student("Male", 20 + i, f"Name{i}", f"Surname{i}", f"RB{i}"))
    except GroupLimitError as e:
        print("\nException caught:", e)

    print("\nFinal group:")
    print(gr)


if __name__ == "__main__":
    run_demo()