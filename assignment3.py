import random
correctans = random.randint(1,100)
gameover = False
n = 2
while gameover == False:
 for x in range (n):
    guess = int(input('Guess a number between 1 and 100'))
    if guess == correctans:
        compare = 'right'
        gameover = True
    elif guess > correctans:
        compare = 'high'
    elif guess < correctans:
        compare = 'low'

    if compare == 'right':
        print('correct,you win')
    elif compare == 'high':
        print('too high, guess again')
    elif compare == 'low':
        print('too low,guess again')