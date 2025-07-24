import math

class Calculator:
    def _init_(self):
        # Initialize the dictionary with basic operations
        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': self.safe_divide
        }

    def safe_divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return x / y

    def add_operation(self, symbol, function):
        # Add a new operation to the dictionary
        self.operations[symbol] = function

    def calculate(self, num1, operator, num2=None):
        # Check if inputs are numbers
        if not isinstance(num1, (int, float)):
            raise ValueError("First input is not a valid number.")
        if num2 is not None and not isinstance(num2, (int, float)):
            raise ValueError("Second input is not a valid number.")

        # Check if the operation is supported
        if operator not in self.operations:
            raise ValueError(f"Unsupported operation '{operator}'.")

        # Perform the operation
        if num2 is not None:
            return self.operations[operator](num1, num2)
        else:
            return self.operations[operator](num1)


# Define advanced mathematical functions
def exponentiation(x, y):
    return math.pow(x, y)

def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(x)

def logarithm(x):
    if x <= 0:
        raise ValueError("Logarithm is only defined for positive numbers.")
    return math.log(x)


# Main program
if __name__ == "_main_":
    calc = Calculator()

    # Add advanced operations
    calc.add_operation('^', exponentiation)
    calc.add_operation('sqrt', square_root)
    calc.add_operation('log', logarithm)

    print("=== Advanced Calculator ===")
    print("Available operations: +, -, *, /, ^, sqrt, log")

    while True:
        try:
            op = input("\nEnter operation symbol (or 'exit' to quit): ")
            if op.lower() == 'exit':
                print("Goodbye!")
                break

            num1_input = input("Enter first number: ")
            num1 = float(num1_input) if '.' in num1_input else int(num1_input)

            if op in ['+', '-', '*', '/', '^']:
                num2_input = input("Enter second number: ")
                num2 = float(num2_input) if '.' in num2_input else int(num2_input)
                result = calc.calculate(num1, op, num2)
            elif op in ['sqrt', 'log']:
                result = calc.calculate(num1, op)
            else:
                print("Invalid operation.")
                continue

            print("Result:", result)

        except Exception as e:
            print("Error:", e)