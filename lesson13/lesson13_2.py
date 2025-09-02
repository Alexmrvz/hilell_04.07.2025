class Counter:

    def __init__(self, current: int = 1, min_value: int = 0, max_value: int = 10) -> None:
        self.current: int = current
        self.min_value: int = min_value
        self.max_value: int = max_value

    def set_current(self, start: int) -> None:
        if start < self.min_value or start > self.max_value:
            raise ValueError("Початкове значення поза межами мінімального та максимального значення")
        self.current = start

    def set_max(self, max_max: int) -> None:
        if max_max < self.min_value:
            raise ValueError("Максимальне значення не може бути менше мінімального")
        if self.current > max_max:
            raise ValueError("Поточне значення перевищує нове максимальне значення")
        self.max_value = max_max

    def set_min(self, min_min: int) -> None:
        if min_min > self.max_value:
            raise ValueError("Мінімальне значення не може бути більше максимального")
        if self.current < min_min:
            raise ValueError("Поточне значення менше нового мінімального значення")
        self.min_value = min_min

    def step_up(self) -> None:
        if self.current >= self.max_value:
            raise ValueError("Достигнут максимум")
        self.current += 1

    def step_down(self) -> None:
        if self.current <= self.min_value:
            raise ValueError("Достигнут минимум")
        self.current -= 1

    def get_current(self) -> int:
        return self.current

if __name__ == "__main__":
    counter = Counter()
    counter.set_current(7)
    counter.step_up()
    counter.step_up()
    counter.step_up()
    assert counter.get_current() == 10, 'Test1'
    try:
        counter.step_up()  # ValueError
    except ValueError as e:
        print(e)  # Достигнут максимум
    assert counter.get_current() == 10, 'Test2'

    counter.set_min(7)
    counter.step_down()
    counter.step_down()
    counter.step_down()
    assert counter.get_current() == 7, 'Test3'
    try:
        counter.step_down()  # ValueError
    except ValueError as e:
        print(e)  # Достигнут минимум
    assert counter.get_current() == 7, 'Test4'