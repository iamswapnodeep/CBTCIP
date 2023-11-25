''' TASK - 1:
ROCK PAPER SCISSOR GAME-->
    Winning Rules as follows:
        Rock vs paper-> paper wins
        Rock vs scissor-> Rock wins
        paper vs scissor-> scissor wins. '''

import random

action = ['rock', 'paper', 'scissors']
player_score = 0
com_score = 0

#Get the input for user:
def get_user_choice():
    choice = input("Enter Your choice (rock/paper/scissors): ").lower()
    if choice not in action:
        print("Invalid Choice!")
        choice = get_user_choice()
    return choice
#Get computer choice:
def get_com_choice():
    return random.choice(action).lower()
#Determine Winner:
def compare(user, com):
    if user == com:
        return "It's a tie !"
    elif (user == 'rock' and com == 'scissors') or (user == 'paper' and com == 'rock') or (user == 'scissors' and com == 'paper'):
        player_score += 1
        return "You WON !"
    else:
        com_score += 1
        return "Computer WON !"

#Main Game:
rounds = int(input("Enter no. of rounds:"))
for round in range(rounds):
    print("\nRound {}:\n".format(round+1))
    user_choice = get_user_choice()
    com_choice = get_com_choice()
    print("User: {} | Computer: {}\n".format(user_choice, com_choice))
    Result = compare(user_choice, com_choice)
    print(Result)

if com_score == player_score:
    print("Match Tied !")
elif com_score > player_score:
    print("Computer Won This Game ! Better Luck Next Time.")
else:
    print("Congrats ! You Won This Game.")