def add_one(some_list):


    num = int(''.join(map(str, some_list)))
    num += 1
    return [int(digit) for digit in str(num)]

print(add_one([1, 2, 3, 4]))
print(add_one([9, 9, 9]))
print(add_one([0]))
print(add_one([9]))