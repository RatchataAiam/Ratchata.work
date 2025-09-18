"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""
import random
def Rnumber():
    random_number=random.randint(1,20)
    MG=8
    for i in range(1,MG):
        if i==7:
            print(f"Random number is {random_number}")
            print("You ran out of Attempt! :(")
            break
        GN=int(input("Enter Your Guess: "))
        if GN>random_number:
            print("Too high! Try again.")
        elif GN<random_number:
            print("Too low! Try again.")
        elif GN==random_number:
            print(f"Congratulations! You Won in {i} attempts")
            print(f"Random number is {random_number}")
            break

Rnumber()
""