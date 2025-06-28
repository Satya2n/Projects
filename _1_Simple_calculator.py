# Simple Calculator in Python
# This code implements a basic calculator that can perform addition, subtraction, multiplication, and division
# This code implements a simple calculator that can add, subtract, multiply, and divide two numbers
# It handles invalid inputs and allows the user to exit the program gracefully
# The calculator runs in a loop until the user decides to exit
# The code is structured to be user-friendly and robust against common input errors
# The main function orchestrates the flow of the program, ensuring a smooth user experience
# The calculator can be extended with more operations or features in the future
# The code is written in Python and can be run in any Python environment

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Cannot divide by zero"

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def main():
    print("Welcome to the simple calculator!")
    while True:
        try:
            operation = input("Choose operation (+, -, *, /) or 'exit' to quit: ").strip().lower()

            if operation == 'exit':
                print("Exiting the calculator. Goodbye!")
                break

            if operation not in operations:
                print("Invalid operation. Please try again.")
                continue

            # Ask for numbers only after a valid operation is selected
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            result = operations[operation](num1, num2)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            print(f"The result is: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()


# This code is a simple calculator that performs basic arithmetic operations
