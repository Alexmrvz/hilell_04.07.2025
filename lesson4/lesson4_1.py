lst = [1, 0, 13, 0, 0, 0, 5]
zeros = []
for x in lst:
    if x == 0:
        zeros.append(x)
while 0 in lst:
    lst.remove(0)
lst = lst + zeros
print(lst)