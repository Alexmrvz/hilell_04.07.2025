import random
length = random.randint(3, 10)
list = [random.randint(1, 10) for _ in range(length)]
print(list)
selected = [list[0], list[2], list[-2]]
print(selected)