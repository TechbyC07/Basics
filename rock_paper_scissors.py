# ask user for choice
import random
  
full_name = {'r': 'rock', 'p':'Paper', 's':'Scissors'}
choices = ('r', 'p', 's')

while True:
    user_choice = input('Rock, Paper, Scissors? (r,p,s) ').lower()
    if user_choice not in choices:
        print('Invalid choice gng') 
        continue

    computer_choice = random.choice(choices)

    print(f'You chose {full_name[user_choice]}')
    print('to try beat')
    print(f', {full_name[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie!')
    elif (user_choice == 'r' and computer_choice == 's') or \
     (user_choice == 'p' and computer_choice == 'r') or \
     (user_choice == 's' and computer_choice == 'p'):
        print('You win')
    else:
        print('You lose ths round')

    move_forward = input('continue? (y/n): ').lower()
    if move_forward == 'n':
        break


#if not then terminate