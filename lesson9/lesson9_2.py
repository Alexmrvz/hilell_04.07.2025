from typing import Union, Tuple


def difference(*numbers: Union[int, float]) -> float:
    if not numbers:
        return 0.0
    return round(max(numbers) - min(numbers), 2)

# print(difference(1, 2, 3))
# print(difference(5, -5))
# print(difference(10.2, -2.2, 0, 1.1, 0.5))
# print(difference())

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
