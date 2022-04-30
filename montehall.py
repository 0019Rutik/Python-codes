import  random 

doors  =[0]*3
goatdoor =[0]*2
swap =0
no_swap =0
j=0
while(j < 10):
    x = random.randint(0,2)
    doors[x] ='BMW'
    for i in range(0,3):
        if (i == x):
            continue
        else:
            doors[i]='goat'
            goatdoor.append(i)
    choice = int(input('Enter The Number'))
    door_open=random.choice(goatdoor)
    if(choice == door_open):
        door_open = random.choice(goatdoor)

    ch = input('choose y to swap  and n to no_swap ?y/n')
    if(ch == 'y'):
        if(doors[choice] == 'goat'):
            print('You win!!')
            swap=swap+1
        else:
            print('you lost')
        
    else:
        if(doors[choice] == 'goat'):
            print('You lose')
        else:
            print('player wins')
            no_swap=no_swap+1
    j=j+1

print(swap)
print(no_swap)
    
    


