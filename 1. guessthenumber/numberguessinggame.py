# Number guessing game.
# Use while loop, if-else, ...


import random
from art import logo
# from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Choose a difficulty. Type 'easy' or 'hard': ")

number = random.randint(1, 100)

while True:
    choice = input()
    if choice == "easy":
        attempts = 10
        break
    elif choice == "hard":
        attempts = 5
        break
    else:
        print("Please type again")

while True:
    print(f"You have {attempts} attempts remaining to guess the number.")
    print("Make a guess:")

    # Input validation loop for an integer
    while True:
        try:
            choice2 = int(input())
        except:
            print("Please re-input an integer:")
        else:
            break
    if choice2 == number:
        print("Congrats! You won!")
        break
    else:
        attempts -= 1
        if attempts == 0:
            print("Sorry. You lost!")
            break
        else:
            if choice2 < number:
                print("Too low. Please try again!")
            else:
                print("Too high. Please try again!")

exit()
