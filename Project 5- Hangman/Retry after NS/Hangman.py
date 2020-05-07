def Hangman (word):
    print ('Guess the word')
    word = word.upper()
    thomas = [x for x in word]
    tom = [x for x in word]
    tum = [x for x in '_'*len(word)]
    print (tum)
    print('\n')
    tries = 0
    failed = []
    while thomas.count('_') != len(tom) and tries != 10:
        guess = input('Guess a letter: ')
        while len(guess) != 1 or not guess or guess in '1234567890' or guess in tum or guess.upper() in failed:
            if len(guess) != 1 or not guess or guess in '1234567890':
                guess = (input('That is not a letter, please guess again: ')).upper()
            if guess in tum or guess.upper() in failed:
                guess = (input('Have already guessed that before, please try again: ')).upper()
        guess = guess.upper()
        if guess not in tom:
            failed.append(guess)
        tim = (''.join(thomas)).replace(guess,'_')
        thomas = [x for x in tim]
        tum = [x if x not in thomas else '_' for x in tom]
        print (tum)
        print ('You have ' +str(10 - tries - 1)+ ' tries left!')
        print ('\n')
        tries += 1
    return tries if thomas.count('_') == len(tom) else 0

def genre ():
    import random
    print ('You can choose one of following genres:')
    genre = ['1: Movies', '2: Occupation', '3: Animals']
    print (genre)
    Genre = input('Choose 1/2/3: ')
    if Genre not in ['1','2','3']:
        print('That is not one of the given options, please choose again')
        Genre = input()
    if Genre == '1':
        print('\n You have chosen: Movies \n')
        choice = random.choice(['Harry Potter', 'Iron Man', 'Man in Black','Star Wars', 'Frozen', 'Thor','Avengers'])
    elif Genre == '2':
        print('\n You have chosen: Occupation \n')
        choice = random.choice(['Teacher','Firefighter','Policeman', 'Driver', 'Soldier','Scientist','Astronaut', 'Pilot','Doctor','Nurse','Barber','Optician', 'Therapist'])
    else:
        print('\n You have chosen: Animals \n')
        choice = random.choice(['Tiger','Lion','Cat','Whale','Octopus','Dolphin','Porcupine','Monkey','Gorilla','Chimpanzee','Starfish','Orca','Dog','Wolve','Crow','Squirrel','Platypus','Scorpion','Spider','Bumblebee'])
    return choice

def Retry():
    Tom = input('Do you want to play again? (Y/N): ')
    if Tom == 'Y':
        hangman()
    elif Tom == 'N' :
        print('Hope you had Fun!!!')
    else:
        print('Bro can you read?')
        Retry()

def hangman():
    print ('Welcome to HANGMAN! \n')
    print ('You will have 10 guesses to guess the word \n')
    choice = genre()
    attempts = Hangman(choice)
    if attempts == 0:
        print ('Too Bad! The word was ' +str(choice)+ '!')
        Retry()
    else:
        print('Congratz, you successfully guessed the word in ' +str(attempts)+ ' tries!')
        Retry()
        
hangman()





