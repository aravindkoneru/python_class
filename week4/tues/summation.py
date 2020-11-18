# Goal: Write a program that accepts 10 numbers from the user, sums them up, 
#   - prints 1 if the total is greater than 100
#   - prints 2 if the total is greater than 50 
#   - prints 3 if the total is greater than 0
#   - prints 4 otherwise
# Print all of the numbers that the user entered and the sum at the end of the program

numbers_limit = 10
user_input = []

# 1. collecting all the numbers from the user and storing in user_input
while len(user_input) < numbers_limit:
    number = int(input("Put in your number: "))
    user_input.append(number)

# 2. summing all the numbers from user_input
print(user_input)

# 3. 
