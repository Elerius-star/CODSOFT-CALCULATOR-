# Step 1: Display a welcome message
print("Welcome to the Simple Calculator!")

# Step 2: Prompt the user for inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 3: Prompt the user for operation choice
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = input("Enter the number corresponding to the operation (1/2/3/4): ")

# Step 4: Perform the calculation
if operation == '1':
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif operation == '2':
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif operation == '3':
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif operation == '4':
    if num2 != 0:  # Check for division by zero
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation choice. Please run the program again.")