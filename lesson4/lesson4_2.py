lst = []
result = 0
if len(lst) == [0]:
    result = 0
else:
    sum_of_even = 0
    for i in range(0, len(lst), 2):
        sum_of_even += lst[i]
        result = sum_of_even * lst[- 1]
print(result)