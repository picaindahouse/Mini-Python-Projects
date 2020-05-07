def Retry():
    Tom = input('Do you want to play again? (Y/N): ')
    if Tom == 'Y':
        Main_Game()
    elif Tom == 'N' :
        print('Hope you had Fun!!!')
    else:
        print('Bro can you read?')
        Retry()
def tortoise ():
    print('Distance will be measured in meters and velocity in meter per second')
    print ('Welcome to the annual Tortoise Race Finals')
    print ('We are down to our final two competitors')
    distance = int(input('The distance the two tortoise will travel in their race is: '))
    print('In honour of reaching the finals they are going to be named by you')
    tortoise1 = input ('Let us start by choosing the name for our first tortoise: ')
    tortoise2 = input ('Now let us choose the name for our second tortoise: ')
    print ("3 2 1, Let's go!")
    print ('It seems like ' +str(tortoise2)+ ' was distracted and has yet to start to racing')
    print ('After much persuasion ' +str(tortoise2)+ ' has started racing')
    print ('However, ' +str(tortoise1)+ ' has quite a significant lead- do you think ' +str(tortoise2)+ ' will be able to catch up?')
    v1 = int(input('What is the velocity of ' +str(tortoise1)+'?: '))
    v2 = int(input('What is the velocity of ' +str(tortoise2)+'?: '))
    g = int(input('What was the distance '+str(tortoise1)+' was able to cover before ' +str(tortoise2)+ ' started racing?: '))
    if v1 > v2:
        time = int(distance/v1)
        print (str(tortoise1) + ' is the winner of the race, completing the race in an impressive '+str(time)+'s!')
    else:
        remainder = distance - g
        if remainder/v1 > distance/v2:
            time = int(distance/v2)
            print ('Despite having started after ' +str(tortoise1)+ ', '+str(tortoise2)+' still won the race, completing the race in an impressive '+str(time)+'s!')
        else:
            time = int(distance/v1)
            print ('Despite ' +str(tortoise2)+ ' being faster than '+str(tortoise1)+' the delay in starting to race has cost it the race')
            print (str(tortoise1) + ' is the winner of the race, completing the race in an impressive '+str(time)+'s!')
    retry()
    
tortoise()