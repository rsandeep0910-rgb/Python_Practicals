# Python program to perform basic arithmetic operations

# Function to get two numbers from the user
def get_numbers():
    try:
        # The input() function gets user input as a string.
        # int() converts the string input to an integer.
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        # Exit the program if the input is not a number
        exit()

# Get the numbers
a, b = get_numbers()

# Perform arithmetic operations
addition = a + b
subtraction = a - b
multiplication = a * b
# Division will always return a float result in Python 3.
division = a / b
# Modulus returns the remainder of the division.
modulus = a % b
# Exponentiation (power) raises 'a' to the power of 'b'.
exponentiation = a ** b
# Floor division divides and rounds down to the nearest whole number (integer).
floor_division = a // b

# Print the results
print(f"\n--- Results of Arithmetic Operations ---")
print(f"Addition of {a} and {b}: {addition}")
print(f"Subtraction of {a} and {b}: {subtraction}")
print(f"Multiplication of {a} and {b}: {multiplication}")
print(f"Division of {a} by {b}: {division}")
print(f"Modulus (remainder) of {a} by {b}: {modulus}")
print(f"Exponentiation ({a} raised to the power of {b}): {exponentiation}")
print(f"Floor Division of {a} by {b}: {floor_division}")

# Example of handling potential ZeroDivisionError with a try-except block
if b == 0:
    print("\nNote: Division by zero occurred, but a try-except block would normally handle this error.")
