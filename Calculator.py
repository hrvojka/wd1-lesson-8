number_1 = int(input("Enter the first integer number: "))
number_2 = int(input("Enter the second integer number: "))
operation = input("Enter the arithmetic operation (+, -, *, /): ")

if operation == "+":
    result = number_1 + number_2
elif operation == "-":
    result = number_1 - number_2
elif operation == "*":
    result = number_1 * number_2
elif operation == "/":
    result = number_1 / number_2

print(result)


