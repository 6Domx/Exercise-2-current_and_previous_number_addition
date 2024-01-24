# Pseudocode
# 1. Ask for a number input from the user
# 2. Analyze the number and the next 10 consecutive number starting from the given value
# 3. Print the 10 consecutive number starting from the given value


# Asking for a number from the user and making sure it only accepts integers
while True:
    given_value = input("Please input a value:")
    if given_value.isdigit():
        given_value = int(given_value)
    else:
        print("Invalid, Value must be in numbers: ")
        break
    highest_value = given_value + 11

    for i in range(given_value, highest_value):
        sum = given_value + i
        print("GIVEN | PREVIOUS | SUM")
        print(i, "   +   ", given_value, "   =", sum)

        given_value = i
        