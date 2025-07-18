def reverse(lst):
    if len(lst) == 0:
        return []
    lst.insert(0, lst.pop())
    return lst

array_of_numbers = [12, 3, 4, 10]
print(reverse(array_of_numbers))