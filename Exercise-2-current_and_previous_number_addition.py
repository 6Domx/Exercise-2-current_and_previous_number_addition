# Pseudocode
# 1. Ask for a number input from the user
# 2. Analyze the number and the next 10 consecutive number starting from the given value
# 3. Print the 10 consecutive number starting from the given value

initial_value = input("Please input a value:")
if initial_value.isdigit():
    initial_value = int(initial_value)
else:
    print("Invalid, Value must be in numbers: ")