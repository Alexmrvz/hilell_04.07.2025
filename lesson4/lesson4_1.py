lst = [0, 1, 0, 12, 3]
zero_count = lst.count(0)
while 0 in lst:
    lst.remove(0)
for _ in range(zero_count):
    lst.append(0)

print(lst)