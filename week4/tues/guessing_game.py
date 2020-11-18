import random

# Goal: Write a guessing game 

# number is a random int from 0 to 100
number_to_guess = random.randint(0, 100)

guess_limit = 5
guess_count = 0

while guess_count < guess_limit:
    guess = int(input("guess: "))
    guess_count += 1

    if number_to_guess < guess:
        print("you guessed too high, pick a smaller number")

    if number_to_guess > guess:
        print("you guessed too low, pick a bigger number")

    if guess == number_to_guess:
        print("you won!")
        break
else:
    print("sorry you failed")


print(f"The number was: {number_to_guess}")



