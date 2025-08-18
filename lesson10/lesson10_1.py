from typing import Union
from inspect import isgenerator

def pow(x: Union[int, float]) -> Union[int, float]:
    return x ** 2

def some_gen(begin: int, end: int, func) -> None:
    current: Union[int, float] = begin
    for _ in range(end):
        yield current
        current = func(current)

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

