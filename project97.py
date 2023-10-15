import random
targetnum, guessnum = random.randint(1, 10), 0
while targetnum != guessnum:
    guessnum = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')
