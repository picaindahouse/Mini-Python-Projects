from math import sqrt
def solution(a,b,c):
    if (b**2 - 4*a*c) < 0:
        return 0
    soln1 = round((-b + sqrt(b**2 - 4*a*c))/(2*a),3)
    soln2 = round((-b - sqrt(b**2 - 4*a*c))/(2*a),3)
    return (soln1,soln2)
    
def Retry():
    Tom = input('Do you want to solve another equation? (Y/N): ')
    if Tom == 'Y':
        quadratic()
    elif Tom == 'N' :
        print('Hope you had Fun!!!')
    else:
        print('Bro can you read?')
        Retry()
        
def quadratic ():
    print('Let us solve ax**2 + bx + c = 0')
    
    X = input('\n What is the a value: ')
    while X[-1] not in '0123456789':
        print ('Has to be a number')
        X = input('What is the a value: ')
    x = int(X)
    
    Y = input('\n What is the b value: ')
    while Y[-1] not in '0123456789':
        print ('Has to be a number')
        Y = input('What is the b value: ')
    y = int(Y)
    
    Z = input('\n What is the c value: ')
    while Z[-1] not in '0123456789':
        print ('Has to be a number')
        Z = input('What is the c value: ')
    z = int(Z)
    print ('\n Thus you wish to solve: ' +'{}{}{}{}{}{}{}{}'.format(str(x)+'x**2' if x != 0 else '', '' if x == 0 or y <= 0 else ' + ', '' if y >= 0 else ' - ', str(abs(y))+'x' if y != 0 else '',  '' if y == 0 or z <= 0 else ' + ', '' if z >= 0 else ' - ', str(abs(z)) if z != 0 else '','' if x == 0 and y == 0 and z == 0 else ' = 0'))
    correct = input ('Yes/No: ')
    while correct != 'No' and correct != 'Yes':
        correct = input ('Yes/No: ')
    else:
        if correct == 'No':
            quadratic()
    ans = solution(x,y,z)
    if ans == 0:
        print ('This quadratic equation cannot be solved')
        Retry()
    else:
        print ('\n Thus x = ' +str(ans[0])+ ' or x = ' +str(ans[1]))
    Retry()
    
quadratic()
        
        
 
