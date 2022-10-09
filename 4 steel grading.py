i1 = float(input('input Rockwell hardness: '))
i2 = float(input('input Carbon Content: '))
i3 = float(input('input Tensile Strength(kg/cm2): '))

#(i) Rockwell hardness > 50
#(ii) Carbon content > 0.7
#(iii) Tensile strength > 5600 kg/cm2

if ((i1>=0) and (i2>=0) and (i3>=0)):
    
    if ((i1>50) and (i2>0.7) and (i3>5600)):
        print('Grade 10')
        
        
    else:
        if ((i1>50) and (i2>0.7)):
            print('Grade 9')
            
            
        else:
            if ((i2>0.7) and (i3>5600)):
                print('Grade 8')
                
            else:
                if ((i1>50) and (i3>5600)):
                    print('Grade 7')
                
                    
                else:
                    print('Grade 0')
                
        
else:
     print('Error! values cannot be less than 0...')
        
 
    
 
    
input('press any key to exit')