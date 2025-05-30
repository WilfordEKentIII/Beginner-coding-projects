# This program gives the user 10 guesses to guess a number between 50
# If the user doesn't guess the game in 10 guesses then they lose

import random

def askForGuess():
    while True:
        guess= input('> ')

        if guess.isdecimal():
            return int(guess) # Convert the guess to a string
        print('Please enter a valid number between 1 and 100.')

print()
secretNumber = random.randint(1,50) #program selects a random numebr between 1-50
print("I am thiniking of a number between 1 and 50.")

for  i  in range(10):
    print('You have {} guess left.Take a guesss.'.format(10-i))
    
    guess = askForGuess()
    if guess == secretNumber:
         
         break

    if guess < secretNumber:
        print('Your guess is too low.')
    if guess > secretNumber:
        print('Guess is too high.')

#Reveal the result
if guess == secretNumber:
    print('Conngratulaions!You guess the number !')
else:
    print("Sorry I was thinking of this number, {}.".format(secretNumber))
