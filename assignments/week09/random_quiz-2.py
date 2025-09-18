"""
#Question 2: Enhanced Guessing Game with Hints
Develop an enhanced guessing game with intelligent hint system:
Core Features:

Random number between 1-100
Unlimited attempts

Progressive hint system:

    After 3 wrong guesses: Show if number is odd/even
    After 5 wrong guesses: Show if divisible by 3 or 5
    After 7 wrong guesses: Narrow the range to 25-number window
    After 10 wrong guesses: Show first digit
    
Example 
    === Enhanced GUESSING GAME ===
    Guess my number between 1 and 100!
    You have unlimited attempts.

    Attempt 1 - Enter your guess: 10
    Too low! Try again.

    Attempt 2 - Enter your guess: 15
    Too high! Try again.

    Attempt 3 - Enter your guess: 12
    Too low! Try again.
    HINT: The number is even
    
    ...
    
    Attempt 5 - Enter your guess: 20
    Too high! Try again.
    HINT: The number is divisible by 5
    
    ...
    
    Congratulations! You won in 10 attempts!

"""

import random
number=random.randint(1,100)

def get_parity_hint(number):
    if number % 2 == 0:
        return "HINT: The number is even" 
    else:
        return "HINT: The number is odd"

def get_divisibility_hint(number):
    if number % 3 == 0:
        return "HINT: The number is divisible by 3"
    elif number % 5 == 0:
        return "HINT: The number is divisible by 5"
    else:
        return "HINT: The number is NOT divisible by 3 or 5"

def get_range_hint(number, current_min=1, current_max=100):
    # Return narrowed range around the number
    current_min=number-12
    current_max=number+12
    print(f"HINT:The number is between:{range(current_min,current_max)}")
    return

def get_thefirst_digit_hint(number):
    # Retun the first digit of the number
    return f"HINT: The First Digit is {number//10}"

i=1
print("=== Enhanced GUESSING GAME ===")
print("Guess my number between 1 and 100!")
print("You have unlimited attempts.")
while True:
    GN=int(input("Enter Your Guess: "))
    if GN>number:
        print("Too high! Try again.")
        i+=1
    elif i % 10 ==0:
        if GN>number:
            print("Too high! Try again.")
            print(get_thefirst_digit_hint(number))
            i+=1
        else:
            print("Too low! Try again.")
            print(get_thefirst_digit_hint(number))
            i+=1
    elif i % 3 == 0:
        if GN>number:
            print("Too high! Try again.")
            get_parity_hint(number)
            i+=1
        else:
            print("Too low! Try again.")
            get_parity_hint(number)
            i+=1
    elif i % 5 == 0:
        if GN>number:
            print("Too high! Try again.")
            print(get_divisibility_hint(number))
            i+=1
        else:
            print("Too low! Try again.")
            print(get_divisibility_hint(number))
            i+=1
    elif i % 7 ==0:
        if GN>number:
            print("Too high! Try again.")
            print(get_range_hint(number, current_min=1, current_max=100))
            i+=1
        else:
            print("Too low! Try again.")
            print(get_range_hint(number, current_min=1, current_max=100))
            i+=1
    elif GN<number:
        print("Too low! Try again.")
        i+=1
    elif GN==number:
        print(f"Congratulations! You Won in {i} attempts")
        print(f"Random number is {number}")
        break