'''TASK - 1
MASTERMIND GAME
Two players play the game against each other; let's assume Player 1 and Player 2.
    Player 1 plays first by setting a multi-digit number.
    Player 2 now tries his first attempt at guessing the number.
    If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he wins the game and is crowned Mastermind! If not, then Player 1 hints by revealing which digits or numbers Player 2 got correct.
    The game continues till Player 2 eventually is able to guess the number entirely.
    Now, Player 2 gets to set the number and Player 1 plays the part of guessing the number.
    If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind. If not, then Player 2 wins the game.'''

import random

# Generates a secret number:
def generate_secret_no():
    while True:
        digits = int(input("Enter no. of digits: "))
        if digits <= 0:
            print("Invalid Input! Please try again.")
            continue
        break
    min = 10 ** (digits - 1)
    max = (10 ** digits) - 1
    number = random.randint(min, max)
    return number, digits

# User Input:
def input_from_user(digit):
    number = input(f"Enter a number of {digit} digits: ")
    return int(number)

# Guess the secret number:
def check_similar_digits(secret, user):
    secret_number_set = set(str(secret))
    user_number_set = set(str(user))
    correct_digits = secret_number_set.intersection(user_number_set)
    return correct_digits

# Check Result:
def no_of_rounds(secret, user):
    count = 0
    while secret != user:
        count += 1
        similar_digits = check_similar_digits(secret, user)
        print(f"The correct digits are: {list(similar_digits)}")
        user = input_from_user(digit_in_number)
        
    return count + 1
#Main Game:
secret_number, digit_in_number = generate_secret_no()
print(f"A {digit_in_number} digit number has been generated.")

player_guess = input_from_user(digit_in_number)

rounds = no_of_rounds(secret_number , player_guess)

print(f"Player got the correct number in {rounds} rounds")