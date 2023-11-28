'''TASK - 1
MASTERMIND GAME
Two players play the game against each other; let's assume Player 1 and Player 2.
    Player 1 plays first by setting a multi-digit number.
    Player 2 now tries his first attempt at guessing the number.
    If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he wins the game and is crowned Mastermind! If not, then Player 1 hints by revealing which digits or numbers Player 2 got correct.
    The game continues till Player 2 eventually is able to guess the number entirely.
    Now, Player 2 gets to set the number and Player 1 plays the part of guessing the number.
    If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind. If not, then Player 2 wins the game.'''
import os
# Input digits:
def input_digits():
    while True:
        digits = int(input("Enter number of digits:"))
        if digits <= 0:
            print("Invalid! Enter valid number of digits!")
            continue
        break
    return digits

# User Input:
def input_from_user(digits):
    while True:
        number = input(f"Enter a number of {digits} digits: ")
        if len(number) > digits and int(number) < 0:
            print("Invalid input! Please try again...")
            continue
        break

    return int(number)

# Guess the secret number:
def check_similar_digits(secret, user):
    secret_number_set = set(str(secret))
    user_number_set = set(str(user))
    correct_digits = secret_number_set.intersection(user_number_set)
    
    return correct_digits

# Check Result:
def no_of_rounds(secret, user):
    round = 0
    while secret != user:
        round += 1
        similar_digits = check_similar_digits(secret, user)
        print(f"The correct digits are: {list(similar_digits)}")
        user = input_from_user(digit_in_number)
        
    return round + 1

# Game Starts here:
def play_game(digits):
    secret_number = input_from_user(digits)
    os.system('cls')
    print("Secret number of {} digits is set. Start guessing the number...".format(digits))
    guess = input_from_user(digits)
    rounds = no_of_rounds(secret_number , guess)
    
    return rounds

# Main:
def main():
    global digit_in_number
    digit_in_number = input_digits()
    print("Player 1 will set the number and Player 2 will guess.")
    player_2 = play_game(digit_in_number)

    print(f"Player 2 succeed in {player_2} round.")
    print("-"*50)

    if player_2 == 1:
        print("Player 2 is crowned MASTERMIND !")
    else:
        print("Player 2 will set the number and Player 1 will guess.")
        player_1 = play_game(digit_in_number)
    
        print(f"Player 1 succeed in {player_1} round.")
        print("-"*50)
        if player_1 > player_2:
            print(f"Player 1: {player_1} | Player 2: {player_2}\nPlayer 2 is crowned MASTERMIND !")
        elif player_2 > player_1:
            print(f"Player 1: {player_1} | Player 2: {player_2}\nPlayer 1 is crowned MASTERMIND !")
        else:
            print(f"Player 1: {player_1} | Player 2: {player_2}\nIt's a tie!")

if __name__ == "__main__":
    main()