P = float(input('input how much is the payment ($): '))


if P>=0:    
    if (P>3000):
        S = 300
        print('your bonus is:', S,'$')
        
    else:
        if ((P>1600) and (P<=3000)):
            S = (P/10)
            if (S>=240):
                S = 240
                print('your bonus is:', S,'$')
            else:
                print('your bonus is:', S,'$')
            

        else:
            S = (P*0.15)
            if (S<=100):
                S = 100
                print('your bonus is:', S,'$')
            else:
                print('your bonus is:', S,'$')
    
else:
    print('Error! payment (P) must be (P)>=0...')



input('press any key to exit...')

