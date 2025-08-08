for user_input in iter(input, ''):


    number = int(user_input)
    number = abs(number)

    while number > 9:
        product = 1
        for digit in str(number):
            product *= int(digit)
        number = product

    print("Result:", number)