print('WELCOME')

C = float(input('input coursework point: '))
E = float(input('input exam point: '))
SC = ((E+C)/2)


if ((C<=100) and (C>=0) and (E<=100) and (E>=0)):
    if ((C>=20) and (E>=20)):
        if ((SC)>=44 and (SC<45)):
            print('your score=', SC)
            print('You are lucky! Your score is moderated to 45...')
            print('Congratulations, you passed :)')
            
        else:
            if (SC<44):
                print('your score=', SC)
                print("You're fail!") 
            else:
                print('your score=', SC)
                print('☆ ☆ Congratulations ☆ ☆')
            
        
    else:
        print('your score=', SC)
        print("You're fail! all points (P) must be (P)>=20...")
    
else:
    print('Error! points (P) must be 0<=(P)<=100... Try Again!')
    
    
input('press any key to exit...')