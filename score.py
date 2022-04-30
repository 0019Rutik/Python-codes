def game():
    return "700"

score = game() 

with open("hiscore.txt") as f:
  his = str(f.read())

  if his=='':
     with open("hiscore.txt",'w') as f:
        f.write(str(score))

if his<score:
     with open("hiscore.txt",'w') as f:
        f.write(str(score))

                