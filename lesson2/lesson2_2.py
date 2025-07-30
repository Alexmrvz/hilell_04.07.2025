number = int(input("Enter a 5 - digit number"))

a, number = divmod(number, 10)
b, number = divmod(number, 10)
c, number = divmod(number, 10)
d, number = divmod(number, 10)
e = number

reversed_number = a + b * 10 + c * 100 + d * 1000 + e * 10000

print(reversed_number)