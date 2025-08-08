results = ()

for user_input in iter(input, ''):
    if not user_input.isdigit():
        print("Invalid input.")
        continue

    number = int(user_input)

    while number > 9:
        product = 1
        for digit in str(number):
            product *= int(digit)
        number = product

    print("Result:", number)

    results = results + (number,)

print("All results:", results)