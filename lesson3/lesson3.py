def calculator(num1, num2, operation):
    try:
        result = ""
        if operation == "+":
            result = num1+num2
        if operation == "-":
            result = num1-num2
        if operation == "*":
            result = num1*num2
        if operation == "/":
            if num2 == 0 or num2 == 0:
                print("dividing to zero is impossible!")
            else:
                result = num1/num2
        print(result)
        return result
    except ValueError:
        print("Enter a valid number")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operator = input("Enter the operation: ")
calculator(number1, number2, operator)

