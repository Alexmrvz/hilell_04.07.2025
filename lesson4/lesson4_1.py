lst = [0, 1, 0, 12, 3]
zero_count = lst.count(0)
non_zeros = [x for x in lst if x != 0]
lst = non_zeros + zero_count * [0]
print(lst)