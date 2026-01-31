while True:
    a = float(input("Enter the first number: "))
    op = input("Enter an action (+, -, *, /): ")
    b = float(input("Enter the second number: "))

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            result = "Error: division by zero!"
        else:
            result = a / b
    else:
        result = "Unknown operation!"

    print("Result:", result)

    cont = input("Would you like to continue? (y/yes): ").lower()
    if cont not in ("y", "yes"):
        print("The work is completed.")
        break
