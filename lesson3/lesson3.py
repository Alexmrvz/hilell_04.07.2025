try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operator = input("Enter the operation (+, -, *, /): ")
    result = ""

    if operator == "+":
        result = number1 + number2

    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":

        if number2 == 0:
            print("Dividing by zero is impossible!")
        else:
            result = number1 / number2
    else:
        print("Invalid operation!")

    if result != "":
        print("Result:", result)

except ValueError:
    print("Enter a valid number")
