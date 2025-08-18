from typing import Generator


def generate_cube_numbers(end: int) -> Generator[int, None, None]:
    num = 2
    while True:
        cube = num ** 3
        if cube > end:
            return
        yield cube
        num += 1

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test1'
assert list(generate_cube_numbers(10)) == [8], 'Test2'
assert list(generate_cube_numbers(100)) == [8, 27, 64], 'Test3'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], 'Test4'
print('Ok')