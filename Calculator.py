x = int(input("Enter the first integer number: "))
y = int(input("Enter the second integer number: "))
operation = input("Enter the arithmetic operation (+, -, *, /): ")

if operation == "+":
    print(x+y)
elif operation == "-":
    print(x-y)
elif operation == "*":
    print(x*y)
elif operation == "/":
    print(x/y)
else:
    print("Please enter the correct arithmetic operation.")