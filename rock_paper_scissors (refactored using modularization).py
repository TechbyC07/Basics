# ask user for choice
import random

full_name = {'r': 'rock', 'p':'Paper', 's':'Scissors'}
choices = (tuple(full_name.keys()))

 
def get_user_choice():
    while True:
        user_choice = input('Rock, Paper, Scissors? (r,p,s) ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice gng!') 

def display_choices(user_choice, computer_choice):
    print(f'You chose {full_name[user_choice]}')
    print('to try beat')
    print(f', {full_name[computer_choice]}')
   
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (user_choice == 'r' and computer_choice == 's') or \
     (user_choice == 'p' and computer_choice == 'r') or \
     (user_choice == 's' and computer_choice == 'p'):
        print('You win')
    else:
        print('You lose ths round')

def play_game():
    while True:
        user_choice =  get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        move_forward = input('continue? (y/n): ').lower()
        if move_forward == 'n':
            break

play_game()
#if not then terminate