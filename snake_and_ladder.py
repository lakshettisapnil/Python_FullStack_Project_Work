import random
import sys

player_1 = input("Enter player_1 name: ").title
player_2 = input("Enter player_2 name: ").title

snack_bite = {98:2,92:82,86:46,82:62,75:55,79:49,67:59,60:30,52:20,22:8}
ladder = {4:16,7:24,9:19,15:32,13:36,24:84,26:42,31:61,39:89,44:88,56:78}
player1_score = 0
player2_score = 0
winning_point = 100

def dice():
    return random.randint(1,6)
def player1_turn():
    global player1_score
    dice_score = dice()
    choice = input("Enter your choice [c] continue or [q] quite: ").lower()
    if choice == 'q':
        print(f'{player_2} congrats Your won the game!')
        sys.exit()
    elif choice == 'c':
        player1_score+=dice_score
        print(f'{player_1} dice rolled: {dice_score}')
    if player1_score in snack_bite:
        player1_score = snack_bite[player1_score]
        print(f'Oops! snack bite ur core is {player1_score}')
    elif player1_score in ladder:
        player1_score = ladder[player1_score]
        print(f'Yeah! you got ladder ur score is {player1_score}')
    print(f'{player_1} Score is: {player1_score}')
def player2_turn():
    global player2_score
    dice_score = dice()
    choice = input("Enter your choice [c] continue or [q] quite: ").lower()
    if choice == 'q':
        print(f'{player_1} congrats Your won the game!')
        sys.exit()
    elif choice == 'c':
        player2_score+=dice_score
        print(f'{player_2} dice rolled: {dice_score}')
    if player2_score in snack_bite:
        player2_score = snack_bite[player2_score]
        print(f'Oops! snack bite ur core is {player2_score}')
    elif player2_score in ladder:
        player2_score = ladder[player2_score]
        print(f'Yeah! you got ladder ur score is {player2_score}')
    print(f'{player_2} Score is: {player2_score}')

while player1_score < 100 and player2_score < 100:
    player1_turn()
    if player1_score >= 100:
        print(f'Congrats {player_1} You Won the game!')
        break
    player2_turn()
    if player2_score >= 100:
        print(f'Congrats {player_2} You won the game!')
        break 
print("Game over Lets Click continue next Game!")
print(f'{player_1} Score is : {player1_score}')
print(f'{player_2} Score is : {player2_score}')
      




    
