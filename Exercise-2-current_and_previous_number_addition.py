# Pseudocode
# 1. Ask for a number input from the user
# 2. Analyze the number and the next 10 consecutive number starting from the given value
# 3. Print the 10 consecutive number starting from the given value

given_value = input("Please input a value:")
if given_value.isdigit():
    given_value = int(given_value)
else:
    print("Invalid, Value must be in numbers: ")

highest_value = given_value + 10

for i in range(1, highest_value):
    sum = given_value + i
    print("Current number is =", i, " Previous Number is =", given_value, " Sum =", sum,)

given_value = i
    