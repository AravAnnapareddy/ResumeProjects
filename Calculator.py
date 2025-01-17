def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        return "Error Divison by Zero"
    return x / y


def main():
    print("Select Operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")
    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print(f"{num1} + {num2} = {add(num1,num2)}")

        elif choice == "2":
            print(f"{num1} - {num2} = {subtract(num1,num2)}")

        elif choice == "3":
            print(f"{num1} * {num2} = {multiplication(num1,num2)}")

        elif choice == "4":
            print(f"{num1} / {num2} = {division(num1,num2)}")

    else:
        print("Invalid Input")

main()
