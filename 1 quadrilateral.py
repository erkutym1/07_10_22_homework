print ("WELCOME")

S1 = float(input('input length of side 1: '))
S2 = float(input('input length of side 2: '))
S3 = float(input('input length of side 3: '))
S4 = float(input('input length of side 4: '))
AG = float(input('input any interior angle: '))
TS1 = (S2+S3+S4)
TS2 = (S1+S3+S4)
TS3 = (S1+S2+S4)
TS4 = (S1+S2+S3)


if ((S1>0) and (S2>0) and (S3>0) and (S4>0) and (AG>0)):
    if ((TS1>S1) and (TS2>S2) and (TS3>S3) and (TS4>S4)):
        if (AG<180):
            if (AG==90):
                if(S1==S2==S3==S4):
                    print("Hey! It's a Square...")
                else:
                    if ((S1+S2==S3+S4) or (S2+S3==S1+S4) or (S1+S3==S2+S4)):
                        print("Hey' It's a Rectangle...")
                    else:
                        print("Hey! It's an Irregular Quadrilateral...")
                    
            else:
                if(S1==S2==S3==S4):
                    print("Hey! It's a Rhombus...")
                else:
                    if ((S1+S2==S3+S4) or (S2+S3==S1+S4) or (S1+S3==S2+S4)):
                        print("Hey! It's a Parallelogram...")
                    else:
                        print("Hey! It's an Irregular Quadrilateral...")
                
        
        else:
            print("Error! the angle must be less than 180")
        
    else:
        print("Error! sum of 3 sides must be greater than 4th side...")
    
else:
    print("Error! inputs cannot be zero...")
    
    
    
input("press any key to exit...")    