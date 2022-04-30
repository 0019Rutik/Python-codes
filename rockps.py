





def Rock_Paper_Scissor(pp1,pp2,bit1,bit2):
    p1 = int(pp1[bit1])%3
    p2 = int(pp2[bit2])%3
    print(p1)
    print(p2)


    if(player1[p1] ==  player2[p2]):
        print('DRAW')
    elif(player1[p1] == 'Rock' and player2[p2] =='Paper'):
        print('player1 wins!!')
    elif(player1[p1] == 'Rock' and player2[p2] =='Scissor'):
        print('player2 wins!!')
    elif(player1[p1] == 'Paper' and player2[p2] =='Rock'):
        print('player1 wins!!')
    elif(player1[p1] == 'Paper' and player2[p2] =='scissor'):
        print('player2 wins!!')
    elif(player1[p1] == 'Scissor' and player2[p2] =='Rock'):
        print('player2 wins!!')
    elif(player1[p1] == 'Scissor' and player2[p2] =='Paper'):
        print('player2 wins!!')



player1 = {0:'Rock',   1: 'Paper', 2:'Scissor'}
player2 = {0:'Scissor',1: 'Rock',   2:'Paper'}

while(1):
    pp1  = input('Enter The Number')
    pp2  = input('Enter The Numbers')
    bit1 = int(input('Enter Secret bit Numbers between 0,1,2'))
    bit2 = int(input('Enter Secret bit Numbers between 0,1,2'))
    Rock_Paper_Scissor(pp1,pp2,bit1,bit2)
    ch = input('Enter y to break and n Continue ? y/n')
    if(ch == 'y'):
        break                       