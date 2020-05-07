import random

def welcome():
    global n
    print ('How many players are playing? (Max: 10)')
    x = input()
    if x in '12345678910':
        n = int(x)
    else:
        welcome()
        
def username (w):
    player = input('Player ' + str(w)+ ': ')
    return player
    
def players (n):
    player_list = [username(x) for x in range(1,n+1)]
    return player_list
    
def ROUND():
    y = input('How many rounds do you wish to play?: ')
    if y in '12345678910':
        return int(y)
    else: 
        ROUND()

def roll (h, player):
    if h == turns:
        if turns == 1:
            print('Let us start with ' + str(player))
        else:
            print("Let's go AGAIN, starting once again with " +str(player))
    elif h == 0:
        print('The first in this intense sudden death match is ' +str(player))
    else:
        print('Next it is ' + str(player) + "'s turn")
    cool = input('Do you wish to role?: ')
    score = random.choice(range(1,7))
    print (str(player) + ' has rolled a ' +str(score))
    if score <= 3:
        print('Seems like he has quite trashy luck')
    else:
        print('Hmm not bad')
    return (score,player)

def Round(player_list, turns):
    print ('\n Turn ' +str(turns) + ' \n')
    tom = [roll(i,x) for i,x in player_list]    
    winners = [p for s,p in tom if s == max([s for s,p in tom])]
    winner = winners[0]
    redo = 0
    # print(winners)
    if len(winners) == 1:
        print ('The round has been won by ' + str(winner) +'!')
        return winner
    else:
        print('Quite a few are tied- however there can only be one WINNER for each round!')
        print('Let us continue till a winner is decided!')
        redo += 0.1
        Round(enumerate(winners,1), turns + redo)    
        return winner
        
def Retry():
    Tom = input('Do you want to play again? (Y/N): ')
    if Tom == 'Y':
        RolltheDice()
    elif Tom == 'N' :
        print('Hope you had Fun!!!')
    else:
        print('Bro can you read?')
        Retry()
        
def RolltheDice ():
    global turns
    print ('Welcome to Roll the Dice!!!')
    welcome()
    player_l = players(n)
    print('Let us begin!')
    rounds = ROUND()
    turns = 0
    winner_list = []
    while rounds != turns:
        turns += 1
        player_list = enumerate(player_l,turns)
        Winner = Round(player_list, turns)
        winner_list.append(Winner)
    WINNER = [(winner_list.count(x),x) for x in winner_list]
    # print(WINNER)
    who = sorted(WINNER)
    highest = {x for i,x in who if i == who[-1][0]}
    if len (highest) == 1:
        print(str(highest.pop()) + ' has won the game, having won ' + str(who[-1][0]) + ' out of the ' + str(rounds) + " rounds each!!!" if rounds > 1 else " round each!!!")  
    else:
        player_list = list(enumerate({x for i,x in who if i == who[-1][0]}))
        print('No clear winner as ' + str(len(highest))+ ' players have won ' + str(who[-1][0]) + ' rounds!')
        print('Therefore, it is time for a SUDDEN DEATH MATCH!')
        new_highest = Round(player_list, ':OMEGA:')
        print('Having won the Sudden Death Match- THE WINNER IS: ' + str(new_highest) + '!!!')
    Retry()

RolltheDice()

