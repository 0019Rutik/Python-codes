import random


doors = [0]*3
goatdoor = [0]*2
swap =0   # no of swaps wins
dont_swap=0   # dont swap wins
j=0
while(j<10):
    x = random.randint(0,2) # x door will comprise of BMW

    doors [x] = "BMW"
    #print(doors)
    for i in range(0,3):
        if(i == x):
           continue
        else:
           doors[i] ="goat"
           #print(doors)
           goatdoor.append(i)
           print(goatdoor)
    choice = int(input("Enter your Choice"))
    door_open=random.choice(goatdoor)  #open the door comprises of goat 
    while(door_open  == choice):
        door_open = random.choice(goatdoor)
    ch = input("Do you Want To Swap ? y/n")
    if(ch =='y'):
        if(doors[choice] == 'goat'):
           print("player wins")
           swap = swap + 1
        else:
           print("player lost")

    else:
        if(doors[choice] == 'goat'):
            print("player Lost")
        else:
            print("player wins")
            dont_swap =dont_swap + 1
    j=j+1

print(swap)
print(dont_swap)