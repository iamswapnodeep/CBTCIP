''' TASK - 2:
ROCK PAPER SCISSOR GAME-->
    Winning Rules as follows:
        Rock vs paper-> paper wins
        Rock vs scissor-> Rock wins
        paper vs scissor-> scissor wins. '''
import random

action = ['rock', 'paper', 'scissors']


#Get the input for user:
def get_user_choice():
    choice = input("Enter Your choice (rock/paper/scissors): ")
    if choice not in action:
        print("Invalid Choice!")
        choice = get_user_choice()
    return choice.lower()

#Get computer choice:
def get_com_choice():
    return random.choice(action).lower()    

#Main Game:
def play_game():
    player_score = 0
    com_score = 0

    rounds = int(input("Enter no. of rounds:"))
    for round in range(rounds):
        print("\nRound {}:".format(round+1))

        user_choice = get_user_choice()
        com_choice = get_com_choice()
        print("User: {} | Computer: {}".format(user_choice, com_choice))
        
        if user_choice == com_choice:
            print("It's a tie !")
        elif (user_choice == 'rock' and com_choice == 'scissors') or (user_choice == 'paper' and com_choice == 'rock') or (user_choice == 'scissors' and com_choice == 'paper'):
            player_score+=1
            print("You WON !")
        else:
            com_score+=1
            print("Computer WON !")

        print("Score:Player: {} | Computer: {}".format(player_score, com_score))
        print("-"*30)

    if com_score == player_score:
            print("Match Tied !")
    elif com_score > player_score:
        print("Computer Won This Match ! Better Luck Next Time.")
    else:
        print("Congrats ! You Won This Match.")

    print("\nGAME OVER!")

if __name__ == "__main__":
        play_game()