def rock_paper_scissor(num1, num2,bit1,bit2):
    p1 = int(num1[bit1]) %3  
    p2 = int(num2[bit2]) %3 
    print(p1)
    print(p2)
    if(player_one[p1] == player_two[p2]):
        print("DRAW !!")                   
    elif(player_one[p1] == "Rock" and player_two[p2] =="scissor"):
        print("player one wins!!")
    elif(player_one[p1] == "Rock" and player_two[p2] =="paper"):
        print("player two wins!!")
    elif(player_one[p1] == "paper" and player_two[p2] =="scissor"):
        print("player two wins!!")
    elif(player_one[p1] == "paper" and player_two[p2] =="Rock"):
        print("player one wins!!")
    elif(player_one[p1] == "scissor" and player_two[p2] =="Rock"):
        print("player two wins !!")
    elif(player_one[p1] == "scissor" and player_two[p2] =="paper"):
        print("player one wins !!")

player_one={0:'Rock',1:'paper',2:'scissor'}
player_two={0:'paper',1:'Rock',2:'scissor'}
while(1):
    num1 = input("plater 1 ,Enter Your choice")
    num2 = input("plater 2 ,Enter Your choice")
    bit1 =int(input('player 1, Enter the secret bit position'))
    bit2 = int(input('player 2, Enter the secret bit position'))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch = input("Do You Want to continue ? y/n")
    if(ch == 'n'):
        break