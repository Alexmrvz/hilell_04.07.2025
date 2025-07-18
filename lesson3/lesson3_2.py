array_of_numbers = [12, 3, 4, 10]

if len(array_of_numbers) == 0:
    reversed_list = []
else:
    array_of_numbers.insert(0, array_of_numbers.pop())
    reversed_list = array_of_numbers

print(reversed_list)