import random
#loop it all until they terminate
while True:
     choice = input('Do you want to roll the dice? (yes/no): ').lower()
     if choice == 'yes' or choice == 'y':
        die = random.randint(1,6)
        print ( f'({die})')
     elif choice == 'n' or choice =='no' :
        print ("Thankyou for playing.")
        break
     else:
        print('Invalid choice')
#if the user enters 'yes' then gnerate a number '1-6' 
#if they pick 'no' terminate the program  
#if the user picks anything else present a validity error