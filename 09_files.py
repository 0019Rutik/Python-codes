#f = open("sample.txt")
#data = f.read()
#print(data)
#f.close()
# also to create file in the pri
with open('game.txt','r') as f:
    a = f.read() 
with open ('game.txt', 'w') as f:
    a = f.write("me tom yu")
    print(a)
f.close()