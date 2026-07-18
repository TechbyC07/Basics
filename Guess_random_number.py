#generate a number in the range
import random

correct_number = random.randint(1,100) 
#while loop
while True:
   
   try:
      guess = int(input('Guess a number between 1  and 100: '))

      if guess > correct_number:
         print('Too high')
      elif guess < correct_number:
         print('Too low')
      else:
         print('Congrats, good guess.')
         break
      #if guessed number == random number print congratulation message
   except ValueError:
      print('enter a valid number')

   # if number is out range then print validity error 