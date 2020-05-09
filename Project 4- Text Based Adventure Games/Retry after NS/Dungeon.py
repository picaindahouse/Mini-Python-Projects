def Dungeon2 ():
    print ('WARNING: THIS GAME REQURIES YOU TO ANSWER THE QUESTIONS AS PROMPTED \n')
    print ('Failure to do so will mean removal from the game \n')
    Tom = input ('Enter User Name: ')
    print ('A young adventurer named ' + str(Tom)+ ' has stumbled across a low level dungeon')
    print ('He wishes to enter it but is not sure if he is ready')
    retry = 1
    attempts = 0
    success = 0
    while retry != 0:
        Enter = input ('Should he enter the dungeon? Y/N only: ')
        if Enter == 'N':
            print ('The young adventurer decides to go back and prepare himself before entering the dungeon in the future')
            print ('GAME OVER') 
            Retry = input ('Do you wish to retry? Y/N only: ')
            if Retry == 'Y':
                retry = retry
                attempts = attempts + 1
            elif Retry == 'N':
                retry = 0
                success = 1
            else: 
                print ('Question clearly states Y/N only- since you cannot read the question properly, you are not worthy of getting a retry')
                print( 'GAME OVER')
                retry = 0
                success = 4
        
        
        elif Enter == 'Y':
            print ('The Adventurer decides to enter the dungeon in hopes of Wealth & Glory')
            print (str (Tom) + ' has entered the dungeon')
            print ('Before he can get a look at his surroundings he hears a loud screech and sees a goblin rushing towards him')
            Action = input ('He can either- Defend, Attack or Dodge: ')
            
            
            if Action == 'Defend':
                print (str(Tom) + ' attempts to raise his shield to block the incoming attack')
                print ('Unfortunately, he fails to raise it in time and is slaughtered by the goblin')
                Last_Words = input ('Any last words?: ')
                print('GAME OVER')
                Retry = input ('Do you wish to retry? Y/N only: ')
                if Retry == 'Y':
                    retry = retry
                    attempts = attempts + 1
                elif Retry == 'N':
                    retry = 0
                    success = 2
                else: 
                    print ('Question clearly states Y/N only- since you cannot read the question properly, you are not worthy of getting a retry')
                    print( 'GAME OVER')
                    retry = 0
                    success = 4
                
            
            elif Action == 'Dodge':
                print (str(Tom) + ' instinctively attempts to dodge')
                side = input ('In which direction does he turn to dodge the goblin, left or right: ')
                if side == 'left':
                    print ('Unfortunately he trips in his attempt to dodge to the left and is brutally murdered by the Goblin')
                    Last_Words = input ('Any last words?: ')
                    print('GAME OVER')
                    Retry = input ('Do you wish to retry? Y/N only: ')
                    if Retry == 'Y':
                        retry = retry
                        attempts = attempts + 1
                    elif Retry == 'N':
                        retry = 0
                        success = 2
                    else: 
                        print ('Question clearly states Y/N only- since you cannot read the question properly, you are not worthy of getting a retry')
                        print( 'GAME OVER')
                        retry = 0
                        success = 4
                    
                elif side == 'right':
                    print ('He dodges to his right just in time to escape the goblin attack')
                    Action1 = input ('What does he do now? Attack or Run: ')
                    if Action1 == 'Attack':
                        print(str(Tom) + ' acts quickly and draws his sword ready to attack the goblin head on')
                        print ('His sword slash successfully seperates the head of the goblin from the rest of its body')
                        print ('Having slain the goblin ' +str(Tom)+ ' finds himself in an empty room with a chest and a portal')
                        chest= input ('Do you wish to open the chest? Y/N only: ')
                        if chest == 'Y':
                            print (str(Tom) + ' attempts to open the chest')
                            print ('To his horror- upon opening it he finds himself looking at a full set of razor sharp teeth')
                            print ('He does not even have the time to comprehend what has happened before he is devoured by the chest')
                            Last_Words = input ('Any last words?: ')
                            print('GAME OVER')
                            Retry = input ('Do you wish to retry? Y/N only: ')
                            if Retry == 'Y':
                                retry = retry
                                attempts = attempts + 1
                            elif Retry == 'N':
                                retry = 0
                                success = 2
                            else: 
                                print ('Question clearly states Y/N only- since you cannot read the question properly, you are not worthy of getting a retry')
                                print( 'GAME OVER')
                                retry = 0
                                success = 4
                            
                        elif chest == 'N':
                            print (str(Tom) + ' has heard stories about monsters that look like treasure chests in dungeons')
                            print ('They are called mimics and have killed countless young adventurers')
                            print ('He decides to play it safe and looks towards the portal')
                            portal = input ('Do you want to enter the portal? Y only: ')
                            if portal == 'Y':
                                print (str(Tom) + 'returned to the safety of the outside world')
                                retry = 0
                                success = 3
                                print('YOU HAVE CLEARED THE GAME: CONGRATULATIONS')
                                
                            else:
                                print ('Question clearly states Y only- since you cannot read the question properly, you are not worthy of clearing the dungeon')
                                print( 'GAME OVER')
                                retry = 0
                                success = 4
                                
                        else:
                            print ('Question clearly states Y/N only- since you cannot read the question properly, you are not worthy of clearing the dungeon')
                            print( 'GAME OVER')
                            retry = 0
                            success = 4
                            
                    elif Action1 == 'Run':
                        print (str(Tom) + ' frightened by the sudden attack is unable to keep his cool and attempts to run away')
                        print ('However, before he can do so- the goblin recovers from its earlier failed attack and strikes at him again')
                        print ('He is unable to escape this time and is killed by the attack')
                        Last_Words = input ('Any last words?: ')
                        print('GAME OVER')
                        Retry = input ('Do you wish to retry? Y/N only: ')
                        if Retry == 'Y':
                            retry = retry
                            attempts = attempts + 1
                        elif Retry == 'N':
                            retry = 0
                            success = 2
                        else: 
                            print ('Question clearly states Y/N only- since you cannot read the question properly, you are not worthy of getting a retry')
                            print( 'GAME OVER')
                            retry = 0
                            success = 4                  
                    
                    else:
                        print ('Question clearly asks for Attack or Run- since you cannot read the question properly, you are not worthy of clearing the dungeon')
                        print( 'GAME OVER')
                        retry = 0
                        success = 4
                else: 
                    print ('Question clearly states left or right- since you cannot read the question properly, you are not worthy of clearing the dungeon')
                    print( 'GAME OVER')
                    retry = 0
                    success = 4  
                    
                
            elif Action == 'Attack':
                print(str(Tom) + ' acts quickly and draws his sword ready to attack the charging goblin head on')
                print ('His sword slash successfully seperates the head of the goblin from the rest of its body')
                print ('Having slain the goblin ' +str(Tom)+ ' finds himself in an empty room with a chest and a portal')
                chest= input ('Do you wish to open the chest? Y/N only: ')
                if chest == 'Y':
                    print (str(Tom) + ' attempts to open the chest')
                    print ('To his horror- upon opening it he finds himself looking at a full set of razor sharp teeth')
                    print ('He does not even have the time to comprehend what has happened before he is devoured by the chest')
                    Last_Words = input ('Any last words?: ')
                    print('GAME OVER')
                    Retry = input ('Do you wish to retry? Y/N only: ')
                    if Retry == 'Y':
                        retry = retry
                        attempts = attempts + 1
                    elif Retry == 'N':
                        retry = 0
                        success = 2
                    else: 
                        print ('Question clearly states Y/N only- since you cannot read the question properly, you are not worthy of getting a retry')
                        print( 'GAME OVER')
                        retry = 0
                        success = 4  
                    
                    
                elif chest == 'N':
                    print (str(Tom) + ' has heard stories about monsters that look like treasure chests in dungeons')
                    print ('They are called mimics and have killed countless young adventurers')
                    print ('He decides to play it safe and looks towards the portal')
                    portal = input ('Do you want to enter the portal? Y only: ')
                    if portal == 'Y':
                        print (str(Tom) + 'returned to the safety of the outside world')
                        retry = 0
                        success = 3
                        print('YOU HAVE CLEARED THE GAME: CONGRATULATIONS')
                                
                    else:
                        print ('Question clearly states Y only- since you cannot read the question properly, you are not worthy of clearing the dungeon')
                        print( 'GAME OVER')
                        retry = 0
                        success = 4
                    
                else:
                    print ('Question clearly states Y/N only- since you cannot read the question properly, you are not worthy of clearing the dungeon')
                    print( 'GAME OVER')
                    retry = 0
                    success = 4
            else:
                print ('Question clearly gives you three options only- since you cannot read the question properly, you are not worthy of clearing the dungeon')
                print( 'GAME OVER')
                retry = 0
                success = 4   
        else:
            print ('Question clearly states Y/N only- since you cannot read the question properly, you are not worthy of entering the dungeon')
            print( 'GAME OVER')
            retry = 0
            success = 4
    
    if success == 1:
        return str(Tom) + ' made it home safely- BOY WHAT A BORING OPTION YOU CHOSE!'
    elif success == 2:
        return 'So you gave up half way through I see- you were never meant to be an ADVENTURER'
    elif success == 3:
        return 'Not bad you succeeded in ' +str(attempts + 1)+ ' tries'
    elif success == 4:
        return 'Congratulations you are an IDIOT!'
    
    
Dungeon2()  