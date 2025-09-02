import math


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def get_square(self) -> int:
        return self.width * self.height

    def find_dimensions(self, area: int) -> tuple[int, int]:
        for w in range(1, int(math.sqrt(area)) + 1):
            if area % w == 0:
                h = area // w
                return (w, h)
        w = int(math.sqrt(area))
        h = (area + w - 1) // w
        return (w, h)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return False
        return self.get_square() == other.get_square()

    def __add__(self, other) -> 'Rectangle':
        if not isinstance(other, Rectangle):
            raise ValueError("only Rectangle objects")
        total_area = self.get_square() + other.get_square()
        new_width, new_height = self.find_dimensions(total_area)
        return Rectangle(new_width, new_height)

    def __mul__(self, n: int) -> 'Rectangle':
        if not isinstance(n, int):
            raise ValueError("must be an integer")
        if n <= 0:
            raise ValueError("must be a positive number")
        new_area = self.get_square() * n
        new_width, new_height = self.find_dimensions(new_area)
        return Rectangle(new_width, new_height)

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height}, area={self.get_square()})"

if __name__ == "__main__":
    r1 = Rectangle(2, 4)
    r2 = Rectangle(3, 6)
    assert r1.get_square() == 8, 'Test1'
    assert r2.get_square() == 18, 'Test2'

    r3 = r1 + r2
    assert r3.get_square() == 26, 'Test3'

    r4 = r1 * 4
    assert r4.get_square() == 32, 'Test4'

    assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
    print(r1)
    print(r3)
    print(r4)