import time
"""
This is a basic calculator. the functions for now are simple, it can only do Addition, Subtraction, Multiplication
and Division. There is also a conditional logic that ensures numbers cannot be divisible by zero, if you try to divide
a number by using 0 as the denominator, it raises an error. I also added the time module which i used to delay the
calculator loading time and result printing time.
"""
def add(x, y): #This function is used to add two numbers
    return x + y

def subtract(x, y): #This function is used to subtract two numbers
    return x - y

def multiply(x, y): #This function is used to multiply two numbers
    return x * y

def divide(x, y): #This function is used to divide two numbers
    if y == 0: #This is a conditional statement that is used to ensure a number cannot be divisible by 0
        return "Error: Cannot divide by zero!" 
    return x / y

def calculator():
    while True:
        print("Loading calculator.....")
        time.sleep(2) # waits 2 seconds before starting
        
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4 Divide (/)")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5/): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            time.sleep(3)
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))

                print("\nCalculating result....")
                time.sleep(2) # delay 2 seconds before printing result

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            else:
                print("Invalid input. Please enter a valid choice.")


if __name__ == "__main__":
    calculator()


