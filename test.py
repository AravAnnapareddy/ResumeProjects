def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        return "Error"
    return x / y


def main():
    print("Make a Selection: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    selection = input("Enter [1,2,3, or 4]: ")

    if selection in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter a second number: "))

        if selection == "1":
            print(f"{num1} + {num2} = {add(num1,num2)}")

        elif selection == "2":
            print(f"{num1} - {num2} = {subtract(num1,num2)}")

        elif selection == "3":
            print(f"{num1} * {num2} = {multiplication(num1,num2)}")

        elif selection == "4":
            print(f"{num1} / {num2} = {division(num1,num2)}")

    else:
        print("Error")


main()
