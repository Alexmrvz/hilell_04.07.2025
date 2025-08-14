def common_elements():


    set_3 = {x for x in range(0, 100, 3)}  #3
    set_5 = {x for x in range(0, 100, 5)}  #5
    return set_3 & set_5

print(common_elements())