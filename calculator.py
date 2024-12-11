#operation u want to perform 
#inputs 
#perform operation
#ans

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        print("Error: Division by zero is not allowed")
    return a / b

def floordiv(a,b):
    if b == 0:
        print("ZeroDivError: Division by zero is not allowed")
    return a // b 

def remainder(a,b):
    return a % b


def calculator():
    print("Welcome to my command line calculator !")
    print("Here are the below operations to perform")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. FLoor divison")
    print("6. Remainder")
    print("7. Exit")

    while True:
        choice = input("enter ur choice to perform operation.. ")

        if choice == '7':
            print("Existing from the calculator.. Bye")
            break

        if choice in ['1','2','3','4','5','6']:
            try:
                num1 = float(input("enter first number"))
                num2 = float(input("enter second number"))

                if choice == '1':
                    print(f"The result is: {add(num1, num2)}")
                elif choice == '2':
                    print(f"The result is: {sub(num1, num2)}")
                elif choice == '3':
                    print(f"The result is: {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"The result is: {divide(num1, num2)}")
                elif choice == '5':
                    print(f"The result is: {floordiv(num1, num2)}")
                elif choice == '6':
                    print(f"The result is: {remainder(num1, num2)}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        else:
            print("Invalid choice. enter for correct operation")


if __name__ == "__main__":
    calculator()
