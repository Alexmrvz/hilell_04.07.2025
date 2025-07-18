def calculator(num1, num2, operation):
    try:
        # num1 = float(input("Enter the number pls"))
        # operation = input("Enter the operation pls")
        # num2 = float(input("Enter the number pls"))
        result = ""
        if operation == "+":
            result = num1+num2
        if operation == "-":
            result = num1-num2
        if operation == "*":
            result = num1*num2
        if operation == "/":
            if num2 == 0:
                print("dividing to zero is impossible!")
            if num1 == 0:
                print("dividing to zero is impossible!")
            result = num1/num2
        print(result)
        return result
    except ValueError:
        print("Enter a valid number")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operator = input("Enter the operation: ")
calculator(number1, number2, operator)

