number1 = input("Enter a 5 - digit number")
reversed_number = number1[::-1]
if len(number1) != 5:
    print("Error: enter 5 digit number")
else:
    print(reversed_number)