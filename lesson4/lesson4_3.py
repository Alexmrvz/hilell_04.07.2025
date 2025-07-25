import random
length = random.randint(3, 10)
numbers = [random.randint(1, 10) for _ in range(length)]
print(numbers)
selected = [numbers[0], numbers[2], numbers[-2]]
print(selected)