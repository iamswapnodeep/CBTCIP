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
    digits = int(input("Enter no. of digits: "))
    if digits <= 0:
        print("Invalid Input! Please try again.")
        number = generate_secret_no()
    else:
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
    secret_number_set = set(secret)
    user_number_set = set(user)
    correct_digits = secret_number_set.intersection(user_number_set)

    return f"The correct digits are: {list(correct_digits)}"

# Check Result:
def check_result(secret, user):
    if secret == user:
        result = "User has been crowned MASTERMIND !"
    else:
        similar_digits = check_similar_digits(str(secret), str(user))
        print(similar_digits)
        if secret != user:
            user = input_from_user(digit_in_number)
            result = check_result(str(secret), str(user))

    return result

#Main Game:
secret_number, digit_in_number = generate_secret_no()
print(f"A {digit_in_number} digit number has been generated.")

player_guess = input_from_user(digit_in_number)

result = check_result(secret_number , player_guess)

print(result)