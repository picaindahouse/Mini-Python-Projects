import random

def Round ():
    z = input('How many rounds do you wish to play?: ')
    while z not in '12345678910':
        z = input('How many rounds do you wish to play?: ')
    rounds = int(z)
    return rounds
    
def difficulty (rounds):
    global x
    print ('There are 4 levels of difficulty: Easy (1), Medium (2), Hard (3) & Very Hard (4)')
    x = input('What difficulty do you wish to attempt? (1/2/3/4): ')
    while x not in '1234':
        print ('\n\n Please only answer with 1/2/3/4 \n\n')
        x = input('What difficulty do you wish to attempt? (1/2/3/4): ')
    if x == '1':
        return [random.choice(range(1,11)) for x in range(rounds)]
    elif x == '2':
        return [random.choice(range(1,51)) for x in range(rounds)]
    elif x == '3':
        return [random.choice(range(1,101)) for x in range(rounds)]
    elif x == '4':
        return [random.choice(range(1,1001)) for x in range(rounds)]

def clue(tom, number):
    if tom > number:
        print('The number is smaller')
    elif tom < number:
        print('The number is larger')

def Guess (i,number): 
    global lives
    if lives == 0:
        return 0
    print ('Round ' +str(i)+'! \n')
    tom = 10000
    while tom != number:
        if lives == 0:
            print ('Oops you are out of lives')
            return 0
        lives -= 1
        if x == '1':
            tim = input('Guess a number between 1 and 10: ')
            while tim not in ''.join([str(x) for x in range(1,11)]):
                tim = input('Guess a number between 1 and 10: ')
            tom = int(tim)
            clue(tom,number)
        elif x == '2':
            tim = input('Guess a number between 1 and 50: ')
            while tim not in ''.join([str(x) for x in range(1,51)]):
                tim = input('Guess a number between 1 and 50: ')
            tom = int(tim)
            clue(tom,number)
        elif x == '3':
            tim = input('Guess a number between 1 and 100: ')
            while tim not in ''.join([str(x) for x in range(1,101)]):
                tim = input('Guess a number between 1 and 100: ')
            tom = int(tim)
            clue(tom,number)
        elif x == '4':
            tim = input('Guess a number between 1 and 1000: ')
            while tim not in ''.join([str(x) for x in range(1,1001)]):
                tim = input('Guess a number between 1 and 1000: ')
            tom = int(tim)
            clue(tom,number)
        print ('\n Have ' + str(lives)+ ' lives left! \n')
    print ('You have successfully guessed the number!')
    print ('You have ' +str(lives)+ ' lives left!')
    return 1

def Retry():
    Tom = input('Do you want to play again? (Y/N): ')
    if Tom == 'Y':
        game()
    elif Tom == 'N' :
        print('Hope you had Fun!!!')
    else:
        print('Bro can you read?')
        Retry()

def game():
    global lives
    print('Welcome to GUESS THE NUMBER! \n')
    rounds = Round()
    numbers = enumerate(difficulty(rounds),1)
    # print (numbers)
    lives = rounds * 10
    print ('You will have ' +str(lives)+ ' tries to guess ' +str(rounds)+ ' numbers')
    results = [Guess(i,x) for i,x in numbers]
    if 0 in results:
        print('Too Bad!')
        Retry()
    else:
        print ('Congratz!!! You have guessed all the numbers!')
    Retry()

game()


































