l1 = int(input('enter your number'))
l2 = int(input('enter your number'))
count = 0
for i in range(l1,l2+1,2):
    if(count==3 ):
        print(i-1)
        count= count+1
        count=0

    elif(count==4):
        print(i-1)
        count=count+1
    
        
    else:           
        print(i)
            
        count=count+1
        

    
               
    
        

