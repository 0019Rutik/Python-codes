import random

def choose():
    words =['rainbow','computer','science','mathmatics','player','reverse','water','board']
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled


def thank(p1n,p2n, p1,p2):
    print(p1n,'your score is:',p1)
    print(p2n,'your score is:',p2)
    print('Thanks For playing')
    print("Have a nice day!")









def play():
    p1name =input('player 1, Enter your Name\n')
    p2name =input('player 2, Enter Your Name\n')
    pp1=0
    pp2=0
    turn = 0
    while(1):
        #computer selectes word..
        picked_word= choose()
        #create a question 
        qn =jumble(picked_word)
        print(qn)
        #player1
        if turn % 2 == 0:
            print(p1name,"your turn.")
            ans=input("what is in your mind?")
            if ans == picked_word:
                pp1 = pp1+1
                print("Your Score is:",pp1)
            else:
                print('Better luck next time, i Thought:',picked_word)
                c = input('press 1 to continue and 0 to quit:')
                if c==0:
                    thank(p1name,p2name,pp1,pp2)  
                    break  
        
        
        #player2
        else:
            print(p2name,"your turn.")
            ans=input("what is in your mind?")
            if ans == picked_word:
                pp2 = pp2+1
                print("Your Score is:",pp2)
            else:
                print('Better luck next time, i Thought:',picked_word)
                c = input('press 1 to continue and 0 to quit:')
                if c==0:
                    thank(p1name,p2name,pp1,pp2)
                    break  
        turn=turn + 1
       

play()